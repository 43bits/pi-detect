import cv2
from ultralytics import YOLO
import pyttsx3
import time

model = YOLO("yolov8n.pt")
tts = pyttsx3.init()

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
h, w = frame.shape[:2]

# Define yellow line — horizontal across bottom third of frame
LINE_Y = int(h * 0.65)  
last_alert_time = 0
ALERT_COOLDOWN = 4  # seconds between alerts

def speak(text):
    tts.say(text)
    tts.runAndWait()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Draw yellow danger line
    cv2.line(frame, (0, LINE_Y), (w, LINE_Y), (0, 255, 255), 3)
    cv2.putText(frame, "DANGER ZONE", (10, LINE_Y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    results = model(frame, classes=[0], conf=0.5)
    boxes = results[0].boxes

    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        foot_y = y2  # bottom of bounding box = feet position

        # Check if person's feet cross the line
        if foot_y >= LINE_Y:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
            now = time.time()
            if now - last_alert_time > ALERT_COOLDOWN:
                speak("Warning! Please stand back from the yellow line.")
                last_alert_time = now
        else:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("Railway Safety Cam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()