import asyncio
import threading
import sys

from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder
import rclpy
from rclpy.node import Node

from string_interface.srv import MARCO
from std_msgs.msg import String

sys.path.insert(0,
                '/home/human/mycroft-core/skills/marco-chess-voice-skill/stockfish/')
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
        self.active_game = False
        self.player_started = False
        self.last_evaluation = 0.0
        self.stockfish = Stockfish(
            "/home/human/Desktop/stockfish12",
            parameters={'Threads': 16,
                        'Write Debug Log': True})
        self.move_list = []

    @intent_handler(IntentBuilder('Emotion')
                    .require('what')
                    .require('is')
                    .require('my')
                    .require('emotion'))
    def current_emotion(self, message):

        self.speak_dialog('voice.chess.marco.emotion',
                          data={'emotion': self.last_emotion},
                          wait=True)

    @intent_handler(IntentBuilder('Greeting')
                    .require('hello'))
    def current_identity(self, message):

        self.speak_dialog('voice.chess.marco',
                          data={'name': self.last_identity},
                          wait=True)

    @intent_handler('voice.chess.marco.startGame.intent')
    def start_chess_game(self, message):
        self.active_game = True
        player_start = self.ask_yesno('voice.chess.marco.askStart',
                                      data={'name': self.last_identity})
        if player_start == 'no':
            self.speak_dialog('voice.chess.marco.start',
                              data={'name': 'I'},
                              wait=True)
            first_move = self.stockfish.get_best_move()
            self.move_list.append(first_move)
            self.speak_dialog('voice.chess.marco.moveFigure',
                              data={'start': first_move[:2],
                                    'end': first_move[2:]},
                              wait=True)
            self.stockfish.set_position(self.move_list)
        else:
            self.player_started = True
            self.speak_dialog('voice.chess.marco.start',
                              data={'name': 'you'},
                              wait=True)

    @intent_handler('voice.chess.marco.moveFigure.intent')
    def move_figure(self, message):
        if self.active_game:
            start = message.data.get('start')
            end = message.data.get('end')
            move = start + end
            if self.stockfish.is_move_correct(move):
                self.move_list.append(move)
                self.stockfish.set_position(self.move_list)

                self.speak_dialog('voice.chess.marco.moveFigure',
                                  data={'start': start, 'end': end},
                                  wait=True)

                current_evaluation = float(
                    self.stockfish.get_stockfish_evaluation())

                g_move = f'voice.chess.marco.emotion.{self.last_emotion}.good'
                if self.player_started:
                    if self.last_evaluation > current_evaluation:
                        self.speak_dialog(g_move, wait=True)
                    else:
                        self.speak_dialog('voice.chess.marco.badMove',
                                          wait=True)
                else:
                    if self.last_evaluation < current_evaluation:
                        self.speak_dialog(g_move, wait=True)
                    else:
                        self.speak_dialog('voice.chess.marco.badMove',
                                          wait=True)

                marco_move = self.stockfish.get_best_move_time(10000)
                self.move_list.append(marco_move)
                self.speak_dialog('voice.chess.marco.moveFigure',
                                  data={'start': marco_move[:2],
                                        'end': marco_move[2:]})
                self.stockfish.set_position(self.move_list)

            else:
                self.speak('This is an invalid move',
                           wait=True)
        else:
            self.speak('We are currently not playing chess',
                       wait=True)

    @intent_handler(IntentBuilder('getBoard')
                    .require('show')
                    .require('board'))
    def get_board(self, message):
        if self.active_game:
            self.log.info(self.stockfish.get_board_visual())
        else:
            self.speak('We are currently not playing chess',
                       wait=True)

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
            self.no_face = True
            thread = threading.Thread(target=self.run, args=())
            thread.daemon = True
            thread.start()

        def run(self):
            asyncio.run(self.update_identity())

        async def update_identity(self):
            while True:
                self.outer_instance.client.request_identity('Current')
                current_identity = self.outer_instance.ros2_call()

                # if no face is detected and the previous face check was also
                # false, tell the user that he is not visible
                if current_identity == 'NoFace' and self.no_face:
                    self.outer_instance.speak('I can not see you',
                                              wait=True)
                    
                # if no face is detected and there is a previous face detected,
                # use that face again remember that no face was detected
                elif current_identity == 'noFace' and not self.no_face:
                    self.no_face = True
                else:
                    self.outer_instance.last_identity = current_identity
                    self.no_face = False
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
            asyncio.run(self.talker())

        async def talker(self):
            while True:
                await asyncio.sleep(120)
                converse = f'voice.emotion.marco.converse.{self.outer_instance.last_emotion} '
                self.outer_instance.speak_dialog(converse,
                                                 wait=True)


def create_skill():
    return MarcoChessVoice()
