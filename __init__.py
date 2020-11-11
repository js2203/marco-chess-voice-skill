from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder
import rclpy
from rclpy.node import Node

from string_interface.srv import MARCO
from std_msgs.msg import String

class MarcoChessVoice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        rclpy.init(args=None)
        self.log.info('*********** init ************')
        self.client = self.MarcoClientAsync()

    @intent_file_handler('voice.chess.marco.intent')
    def handle_voice_chess_marco(self, message):
        self.client.send_request('Hello')

        while rclpy.ok():
            rclpy.spin_once(self.client)
            if self.client.future.done():
                try:
                    response = self.client.future.result()
                except Exception as e:
                    self.log.info('Service call failed {}'.format(e,))
                else:
                    self.log.info('Result: {}'.format(response.res))
                break
        self.speak('Hello {}'.format(response))

    @intent_handler(IntentBuilder('Greeting')
                    .require('hello'))
    def handle_voice_chess_marco(self, message):

        self.client.request_identity('Current')
        while rclpy.ok():
            rclpy.spin_once(self.client)
            if self.client.future.done():
                try:
                    response = self.client.future.result()
                except Exception as e:
                    self.log.info('Service call failed {}'.format(e,))
                else:
                    self.log.info('Result: {}'.format(response.res))
                break
        self.speak('Hello {}'.format(response))

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


def create_skill():
    return MarcoChessVoice()

