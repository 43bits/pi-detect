from llm.ollama_client import describe_scene
import time

class SceneAnalyzer:
    def __init__(self, interval=30):
        self.interval = interval
        self.last_time = 0

    def analyze(self, frame):
        now = time.time()

        if now - self.last_time < self.interval:
            return None

        self.last_time = now
        return describe_scene(frame)