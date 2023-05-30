import cv2  # Install opencv-python


class Camera:
    image = None
    is_close = False
    def __init__(self, index, title):
        self.camera = cv2.VideoCapture(index)
        self.title = title

    def show_image(self):
        # Grab the webcamera's image.
        ret, image = self.camera.read()
        # Resize the raw image into (224-height,224-width) pixels
        self.image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        if not self.is_close:
            cv2.imshow(self.title, self.image)

        if cv2.waitKey(1) == 27:
            self.is_close = True
            cv2.destroyWindow(self.title)

    def get_image(self):
        return self.image
