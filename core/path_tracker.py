import numpy as np
from collections import defaultdict, deque
from sklearn.ensemble import IsolationForest

class PathTracker:
    def __init__(self):
        self.paths = defaultdict(lambda: deque(maxlen=50))
        self.model = IsolationForest(contamination=0.1)

        # dummy training
        self.model.fit(np.random.rand(50, 4))

    def update(self, track_id, center):
        self.paths[track_id].append(center)

    def is_anomaly(self, track_id):
        path = self.paths[track_id]

        if len(path) < 5:
            return False

        pts = np.array(path)

        speed = np.mean(np.linalg.norm(np.diff(pts, axis=0), axis=1))
        spread = pts.std()
        dist = np.linalg.norm(pts[-1] - pts[0])

        feat = [[speed, spread, dist, len(pts)]]

        pred = self.model.predict(feat)
        return pred[0] == -1