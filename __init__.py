from mycroft import MycroftSkill, intent_file_handler
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class Listener(Node):

    def __init__(self):
        super().__init__('listener')
        self.data = ''
        self.sub = self.create_subscription(String, 'chatter', self.chatter_callback, 10)

    def chatter_callback(self, msg):
        self.data = msg.data

    def get(self):
        return self.data

def main(args=None):
    rclpy.init(args=args)

    node = Listener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

class MarcoChessVoice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.log.info('** init **')
        self.Listen = Listener()
        self.log.info(self.Listen.get())

    @intent_file_handler('voice.chess.marco.intent')
    def handle_voice_chess_marco(self, message):
        self.speak_dialog('voice.chess.marco')


def create_skill():
    return MarcoChessVoice()

