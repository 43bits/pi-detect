import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Downloads ~6MB nano model automatically

cap = cv2.VideoCapture(0)   # 0 = laptop webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, classes=[0], conf=0.5)  # class 0 = person only
    annotated = results[0].plot()

    cv2.imshow("Smart Cam - Phase 1", annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()