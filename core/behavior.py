import time

class BehaviorEngine:
    def __init__(self):
        self.dwell_times = {}

    def check_loitering(self, det):
        tid = det.track_id

        if tid == -1:
            return False

        now = time.time()

        if tid not in self.dwell_times:
            self.dwell_times[tid] = now
            return False

        return (now - self.dwell_times[tid]) > 8