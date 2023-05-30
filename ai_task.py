from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np


class Aitask:
    def __init__(self, get_image):
        print("Init task 1")

        self.get_image = get_image

        np.set_printoptions(suppress=True)
        # Disable scientific notation for clarity

        # Load the model
        self.model = load_model("keras_model.h5", compile=False)

        # Load the labels
        self.class_names = open("labels.txt", "r").readlines()

        # CAMERA can be 0 or 1 based on default camera of your computer
        # self.camera = cv2.VideoCapture(1)

        return

    def run(self):
        print("Task 1 is running!!!")

        image = self.get_image()
        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predicts the model
        prediction = self.model.predict(image)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
