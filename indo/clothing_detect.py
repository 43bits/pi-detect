import cv2
import numpy as np

def detect_dominant_color(frame, x1, y1, x2, y2):
    """Detect the dominant color of the upper half of the person bounding box"""
    torso = frame[y1:y1 + (y2 - y1) // 2, x1:x2]
    if torso.size == 0:
        return "person"

    hsv = cv2.cvtColor(torso, cv2.COLOR_BGR2HSV)
    avg_hue = np.mean(hsv[:, :, 0])
    avg_sat = np.mean(hsv[:, :, 1])

    # Basic color classification
    if avg_sat < 40:
        return "white or grey shirt"
    elif avg_hue < 10 or avg_hue > 170:
        return "red shirt"
    elif 10 <= avg_hue < 30:
        return "orange shirt"
    elif 30 <= avg_hue < 65:
        return "yellow shirt"
    elif 65 <= avg_hue < 85:
        return "green shirt"
    elif 85 <= avg_hue < 130:
        return "blue shirt"
    elif 130 <= avg_hue < 160:
        return "purple shirt"
    else:
        return "dark shirt"