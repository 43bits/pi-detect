import cv2
import numpy as np
from config.settings import CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT

class CameraCapture:
    def __init__(self, source=CAMERA_INDEX):
        self.cap = cv2.VideoCapture(source)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # reduce latency
        if not self.cap.isOpened():
            raise IOError(f"Cannot open camera: {source}")
        print(f"[CAMERA] Opened: {source} @ {FRAME_WIDTH}x{FRAME_HEIGHT}")

    def read(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()

    def is_night(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return np.mean(gray) < 60