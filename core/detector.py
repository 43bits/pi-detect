from ultralytics import YOLO
from config.settings import YOLO_MODEL, YOLO_CONF, YOLO_CLASSES
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Detection:
    x1: int; y1: int; x2: int; y2: int
    conf: float; track_id: int = -1

    @property
    def center(self) -> Tuple[int, int]:
        return ((self.x1 + self.x2) // 2, (self.y1 + self.y2) // 2)

    @property
    def feet(self) -> Tuple[int, int]:
        return ((self.x1 + self.x2) // 2, self.y2)

class HumanDetector:
    def __init__(self):
        self.model = YOLO(YOLO_MODEL)
        print("[YOLO] Model loaded")

    def detect(self, frame) -> List[Detection]:
        results = self.model.track(
            frame,
            classes=YOLO_CLASSES,
            conf=YOLO_CONF,
            persist=True,
            verbose=False
        )
        detections = []
        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            tid = int(box.id[0]) if box.id is not None else -1
            detections.append(Detection(x1, y1, x2, y2, conf, tid))
        return detections