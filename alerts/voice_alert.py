import pyttsx3
import time

class VoiceAlert:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.last_time = 0

    def speak(self, text):
        now = time.time()

        if now - self.last_time < 5:
            return

        self.last_time = now

        self.engine.say(text)
        self.engine.runAndWait()

    def intruder(self, name):
        if name == "UNKNOWN":
            self.speak("Unknown person detected")
        else:
            self.speak(f"{name} detected")