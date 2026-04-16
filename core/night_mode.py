import cv2

def enhance_night(frame):
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    merged = cv2.merge((cl, a, b))
    enhanced = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)

    return enhanced

def preprocess(frame, is_night):
    if is_night:
        frame = enhance_night(frame)

    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    return frame