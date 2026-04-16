import cv2
from core.capture import CameraCapture
from core.detector import HumanDetector
from core.face_recognizer import FaceRecognizer
from core.color_analyzer import get_clothing_color
from alerts.voice_alert import VoiceAlert
from alerts.telegram_bot import TelegramAlert

cam = CameraCapture()
detector = HumanDetector()
face = FaceRecognizer()
voice = VoiceAlert()
telegram = TelegramAlert()

while True:
    frame = cam.read()
    if frame is None:
        break

    detections = detector.detect(frame)

    for det in detections:
        name = face.identify(frame, det)
        color = get_clothing_color(frame, det.x1, det.y1, det.x2, det.y2)

        if name == "UNKNOWN":
            voice.speak("Intruder detected")
            telegram.send(frame, "Unknown person detected")

        cv2.rectangle(frame, (det.x1, det.y1), (det.x2, det.y2), (0,0,255), 2)
        cv2.putText(frame, f"{name} {color}", (det.x1, det.y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

    cv2.imshow("Home Security", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()