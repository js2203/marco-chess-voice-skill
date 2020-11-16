import asyncio
import threading

from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder
import rclpy
from rclpy.node import Node

from string_interface.srv import MARCO
from std_msgs.msg import String

sys.path.insert(0, './stockfish/')
from stockfishEngine import Stockfish


class MarcoChessVoice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        rclpy.init(args=None)
        self.log.info('*********** init ************')
        self.client = self.MarcoClientAsync()
        self.last_emotion = ''
        self.last_identity = ''

        # init the background functions
        self.AsyncIdentityUpdater(self)
        self.AsyncEmotionUpdater(self)
        self.AsyncTalker(self)

        # init the stockfish chess engine
        self.stockfish = Stockfish(
            "",
            parameters={'Threads': 16,
                        'Write Debug Log': True})
        self.move_list = []

    def ros2_call(self) -> String:
        try:
            while rclpy.ok():
                rclpy.spin_once(self.client)
                if self.client.future.done():
                    try:
                        response = self.client.future.result()
                    except Exception as e:
                        self.log.info('Service call failed {}'.format(e, ))
                        return ''
                    else:
                        self.log.info('Result: {}'.format(response.res))
                        return response.res
        except:
            self.log.info('rclpy not ready')
            return ''

    @intent_handler(IntentBuilder('Emotion')
                    .require('what')
                    .require('is')
                    .require('my')
                    .require('emotion'))
    def current_emotion(self, message):

        self.speak_dialog('voice.chess.marco.emotion',
                          data={'emotion': self.last_emotion})

    @intent_handler(IntentBuilder('Greeting')
                    .require('hello'))
    def current_identity(self, message):

        self.speak_dialog('voice.chess.marco',
                          data={'name': self.last_identity})

    @intent_handler(IntentBuilder('moveFigure')
                    .require('move')
                    .require('moveRx'))
    def move_figure(self, message):
        start = message.data.get('start')
        end = message.data.get('end')
        move = start + end
        if self.stockfish.is_move_correct(move):
            self.move_list.append(move)
            self.stockfish.set_position(self.move_list)

            self.speak_dialog('voice.chess.marco.moveFigure',
                              data={'start': start,
                                    'end': end})
        else:
            self.spreak('This is an invalid move')

    @intent_handler(IntentBuilder('getBoard')
                    .require('show')
                    .require('board'))
    def get_board(self, message):
        self.log.info(self.stockfish.get_board_visual())

    class MarcoClientAsync(Node):

        def __init__(self):
            super().__init__('marco_client_async')
            self.emotion_client = self.create_client(MARCO, 'MARCO_emotion')
            self.identity_client = self.create_client(MARCO, 'MARCO_identity')
            while not self.emotion_client.wait_for_service(timeout_sec=1.0):
                self.get_logger().info(
                    'Emotion not available, waiting again...')
            while not self.identity_client.wait_for_service(timeout_sec=1.0):
                self.get_logger().info(
                    'Identity not available, waiting again...')
            self.req = MARCO.Request()

        def request_emotion(self, request):
            self.req.req = request
            self.future = self.emotion_client.call_async(self.req)

        def request_identity(self, request):
            self.req.req = request
            self.future = self.identity_client.call_async(self.req)

    class AsyncIdentityUpdater(object):
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()

        def run(self):
            asyncio.run(self.update_identity())

        async def update_identity(self):
            while True:
                self.outer_instance.client.request_identity('Current')
                self.outer_instance.last_identity = self.outer_instance.ros2_call()
                await asyncio.sleep(5)

    class AsyncEmotionUpdater(object):
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()

        def run(self):
            asyncio.run(self.update_emotion())

        async def update_emotion(self):
            while True:
                self.outer_instance.client.request_emotion('Current')
                self.outer_instance.last_emotion = self.outer_instance.ros2_call()
                await asyncio.sleep(1)

    class AsyncTalker(object):
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()

        def run(self):
            asyncio.run(self.update_emotion())

        async def update_emotion(self):
            while True:
                await asyncio.sleep(120)
                self.outer_instance.speak(
                    f'Why are you {self.outer_instance.last_emotion}?')


def create_skill():
    return MarcoChessVoice()
