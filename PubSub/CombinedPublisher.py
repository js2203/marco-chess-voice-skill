import asyncio
import os
import threading
import tensorflow as tf
import cv2
import numpy as np
from PIL import Image
from glob import glob

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

    def __init__(self, emotion_model_path: str, identity_model_path: str):
        physical_devices = tf.config.experimental.list_physical_devices('GPU')
        assert len(
            physical_devices) > 0, "Not enough GPU hardware devices available"
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
        self.emotion_model = tf.keras.models.load_model(emotion_model_path)
        self.identity_model = tf.keras.models.load_model(identity_model_path)
        self.predicted_emotion = 'unknown'
        self.predicted_identity = 'unknown'

    def emotion_detection(self):

        cap = cv2.VideoCapture(0)

        names = ['Neutral', 'Happiness', 'Sadness', 'Surprise', 'Fear',
                 'Disgust', 'Anger', 'Contempt']
        emotions = sorted(names)

        classes = []
        for name in glob('../FaceDetection/src/people/train/*'):
            classes.append(os.path.basename(name))
        identities = sorted(classes)

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

            if faces == ():
                self.predicted_emotion = 'NoFace'
                pass
            else:
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255),
                                  2)
                faces_only = normalize_faces(frame, faces)
                for face in faces_only:
                    image = Image.fromarray(face, 'RGB')

                    image_array = np.array(image, dtype=np.float32)
                    image_array = np.expand_dims(image_array, axis=0)

                    emotion_array = image_array / 127.5
                    emotion_array -= 1.
                    identity_array = image_array / 255

                    emotion_predictions = self.emotion_model(emotion_array)
                    identity_predictions = self.identity_model.predict(
                        identity_array)

                if identity_predictions[0][np.argmax(
                        identity_predictions)] > 10.0:
                    self.predicted_identity = identities[np.argmax(
                        identity_predictions)]
                else:
                    self.predicted_identity = 'unknown Face'

                self.predicted_emotion = names[np.argmax(emotion_predictions)]

            # web cam params
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottom_left_corner_of_text = (10, 30)
            font_scale = 1
            font_color = (255, 255, 255)
            line_type = 2

            # add text on the image
            cv2.putText(frame, self.predicted_emotion,
                        bottom_left_corner_of_text,
                        font,
                        font_scale,
                        font_color,
                        line_type)
            # add text on the image
            cv2.putText(frame, self.predicted_identity,
                        (10, 60),
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

    def __init__(self, outer_instance, Type):
        self.outer_instance = outer_instance
        self.Type = Type
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        rclpy.init(args=None)
        publisher = self.Type(self.outer_instance)
        rclpy.spin(publisher)
        publisher.destroy_node()
        rclpy.shutdown()


class Publisher(Node):

    def __init__(self, outer_instance):
        super().__init__('emotion_publisher')
        self.publisher_ = self.create_publisher(String, 'Emotion', 10)
        self.publisher_ = self.create_publisher(String, 'Identity', 10)
        self.outer_instance = outer_instance
        emotion_timer_period = 0.1  # seconds
        identity_timer_period = 0.2  # seconds
        self.timer = self.create_timer(emotion_timer_period,
                                       self.emotion_callback)
        self.timer = self.create_timer(identity_timer_period,
                                       self.identity_callback)

    def emotion_callback(self):
        msg = String()
        msg.data = self.outer_instance.predicted_emotion
        self.publisher_.publish(msg)
        self.get_logger().info('emotion_publisher: "%s"' % msg.data)

    def identity_callback(self):
        msg = String()
        msg.data = self.outer_instance.predicted_identity
        self.publisher_.publish(msg)
        self.get_logger().info('identity_publisher: "%s"' % msg.data)


if __name__ == '__main__':
    Detector = webcam_detection(
        'C:\\Users\\janni\\Desktop\\class_weight_affectnet_aug_sub8_jannik_2020-11-05_21-58',
        'C:\\Users\\janni\\Desktop\\BA\\BA_src\\FaceDetection\\src\weights\\vgg16_linear_11-06-2020-17_04.h5')
    BackgroundPublisher(Detector, Publisher)
    Detector.emotion_detection()
