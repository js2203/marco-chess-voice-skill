import asyncio
import threading
from argparse import ArgumentParser
import tensorflow as tf
import cv2
import numpy as np
from PIL import Image

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


def cut_faces(image, faces_coord):
    faces = []
    for (x, y, w, h) in faces_coord:
        faces.append(image[y: y + h, x: x + w])

    return faces


def resize(images, size=(224, 224)):
    images_norm = []
    for image in images:
        if image.shape < size:
            image_norm = cv2.resize(image, size,
                                    interpolation=cv2.INTER_AREA)
        else:
            image_norm = cv2.resize(image, size,
                                    interpolation=cv2.INTER_CUBIC)
        images_norm.append(image_norm)

    return images_norm


def normalize_faces(image, faces_coord):
    faces = cut_faces(image, faces_coord)
    faces = resize(faces)

    return faces


class webcam_detection():

    def __init__(self, model_path: str):
        physical_devices = tf.config.experimental.list_physical_devices('GPU')
        assert len(
            physical_devices) > 0, "Not enough GPU hardware devices available"
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
        self.model = tf.keras.models.load_model(model_path)
        self.predicted_name = 'unknown'

    def emotion_detection(self):

        cap = cv2.VideoCapture(0)

        # web cam params
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottom_left_corner_Of_text = (10, 30)
        font_scale = 1
        font_color = (255, 255, 255)
        line_type = 2

        names = ['Neutral', 'Happiness', 'Sadness', 'Surprise', 'Fear',
                 'Disgust', 'Anger', 'Contempt']
        names = sorted(names)



        # launch web cam
        video_capture = cv2.VideoCapture(0)

        classifier = cv2.CascadeClassifier(
            './haarcascade_frontalface_default.xml')

        exit = False
        while not exit:
            _, frame = video_capture.read()

            faces = classifier.detectMultiScale(
                frame,
                scaleFactor=1.2,
                minNeighbors=4,
                minSize=(100, 100),
                flags=cv2.CASCADE_SCALE_IMAGE)

            self.predicted_name = 'NoFace'
            if faces == ():
                pass
            else:
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                faces_only = normalize_faces(frame, faces)
                for face in faces_only:
                    image = Image.fromarray(face, 'RGB')
                    image_array = np.array(image, dtype=np.float32)
                    image_array /= 127.5
                    image_array -= 1.
                    image_array = np.expand_dims(image_array, axis=0)
                    prediction = self.model(image_array)

            #img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #x = cv2.resize(img, (224, 224))
            #x = np.array(x, dtype=np.float32)
            #x /= 127.5
            #x -= 1.
            #x = np.expand_dims(x, axis=0)
            #prediction = model(x)
                self.predicted_name = names[np.argmax(prediction)]

            # add text on the image
            cv2.putText(frame, self.predicted_name,
                        bottom_left_corner_Of_text,
                        font,
                        font_scale,
                        font_color,
                        line_type)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                exit = True

        cap.release()
        cv2.destroyAllWindows()


class BackgroundPublisher(object):

    def __init__(self, outer_instance):
        self.outer_instance = outer_instance
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        rclpy.init(args=None)
        emotion_publisher = EmotionPublisher(self.outer_instance)
        rclpy.spin(emotion_publisher)
        emotion_publisher.destroy_node()
        rclpy.shutdown()


class EmotionPublisher(Node):

    def __init__(self, outer_instance):
        super().__init__('emotion_publisher')
        self.publisher_ = self.create_publisher(String, 'Emotion', 10)
        self.outer_instance = outer_instance
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.emotion_callback)

    def emotion_callback(self):
        msg = String()
        msg.data = self.outer_instance.predicted_name
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)


if __name__ == '__main__':

    Detector = webcam_detection('C:\\Users\\janni\\Desktop\\class_weight_affectnet_aug_sub8_jannik_2020-11-05_21-58')
    BackgroundPublisher(Detector)
    Detector.emotion_detection()
