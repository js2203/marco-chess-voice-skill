from mycroft import MycroftSkill, intent_file_handler
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MarcoClientAsync(Node):

    def __init__(self):
        super().__init__('marco_client_async')
        self.cli = self.create_client(MARCO, 'MARCO')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = MARCO.Request()

    def send_request(self, request):
        self.req.req = request
        self.future = self.cli.call_async(self.req)


class MarcoChessVoice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        rclpy.init(args=None)
        self.log.info('*********** init ************')
        self.client = MarcoClientAsync()

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
        self.speak_dialog('voice.chess.marco')


def create_skill():
    return MarcoChessVoice()

