import rclpy
from rclpy.node import Node

from string_interface.srv import MARCO
from std_msgs.msg import String


class MarcoClientAsync(Node):

    def __init__(self):
        super().__init__('marco_client_async')
        self.emotion_client = self.create_client(MARCO, 'MARCO_emotion')
        self.identity_client = self.create_client(MARCO, 'MARCO_identity')
        while not self.emotion_client.wait_for_service(timeout_sec=1.0):
            print('Emotion not available, waiting again...')
        while not self.identity_client.wait_for_service(timeout_sec=1.0):
            print('Identity not available, waiting again...')
        self.req = MARCO.Request()

    def request_emotion(self, request):
        self.req.req = request
        self.future = self.emotion_client.call_async(self.req)

    def request_identity(self, request):
        self.req.req = request
        self.future = self.identity_client.call_async(self.req)


class MarcoChessVoice():
    def __init__(self):
        rclpy.init(args=None)
        self.client = MarcoClientAsync()

    def handle_voice_chess_marco(self):
        self.client.request_emotion('Hello')

        while rclpy.ok():
            rclpy.spin_once(self.client)
            if self.client.future.done():
                try:
                    response = self.client.future.result()
                except Exception as e:
                    print('Service call failed {}'.format(e,))
                else:
                   print('Result: {}'.format(response.res))
                break
        print('Hello {}'.format(response))


if __name__ == '__main__':
	client = MarcoChessVoice()
	client.handle_voice_chess_marco()


