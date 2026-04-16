import os
from deepface import DeepFace
from config.settings import FACES_DIR

class FaceRecognizer:
    def __init__(self):
        self.db_path = str(FACES_DIR)

    def identify(self, frame, box):
        x1, y1, x2, y2 = box.x1, box.y1, box.x2, box.y2
        face_crop = frame[y1:y2, x1:x2]

        if face_crop.size == 0:
            return "UNKNOWN"

        try:
            result = DeepFace.find(
                img_path=face_crop,
                db_path=self.db_path,
                enforce_detection=False,
                silent=True
            )

            if result and len(result[0]) > 0:
                identity = result[0]["identity"][0]
                name = os.path.basename(os.path.dirname(identity))
                return name.upper()

        except:
            pass

        return "UNKNOWN"