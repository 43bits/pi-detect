import cv2
import numpy as np

def get_clothing_color(frame, x1, y1, x2, y2):
    torso = frame[y1:y2, x1:x2]

    if torso.size == 0:
        return "person"

    hsv = cv2.cvtColor(torso, cv2.COLOR_BGR2HSV)
    avg_color = np.mean(hsv, axis=(0, 1))

    hue = avg_color[0]

    if hue < 10 or hue > 160:
        return "red"
    elif hue < 25:
        return "orange"
    elif hue < 35:
        return "yellow"
    elif hue < 85:
        return "green"
    elif hue < 130:
        return "blue"
    else:
        return "purple"