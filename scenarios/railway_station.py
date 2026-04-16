import cv2
from core.capture import CameraCapture
from core.detector import HumanDetector
from core.color_analyzer import get_clothing_color
from alerts.voice_alert import VoiceAlert
from config.railway_zone import LINE_Y

cam = CameraCapture()
detector = HumanDetector()
voice = VoiceAlert()

while True:
    frame = cam.read()
    if frame is None:
        break

    detections = detector.detect(frame)

    for det in detections:
        _, foot_y = det.feet

        if foot_y > LINE_Y:
            color = get_clothing_color(frame, det.x1, det.y1, det.x2, det.y2)
            voice.speak(f"Warning person in {color}")

        cv2.rectangle(frame, (det.x1, det.y1), (det.x2, det.y2), (0,255,255), 2)

    cv2.line(frame, (0, LINE_Y), (1280, LINE_Y), (0,255,255), 3)

    cv2.imshow("Railway Safety", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()