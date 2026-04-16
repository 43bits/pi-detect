import requests
import cv2
import time
import threading
from pathlib import Path
from datetime import datetime
from config.settings import TELEGRAM_TOKEN, TELEGRAM_CHAT, SNAPSHOTS, TELEGRAM_COOLDOWN

class TelegramAlert:
    def __init__(self):
        self._last = 0
        self.active = bool(TELEGRAM_TOKEN)
        SNAPSHOTS.mkdir(parents=True, exist_ok=True)

    def send(self, frame, caption):
        if not self.active:
            return

        now = time.time()
        if (now - self._last) < TELEGRAM_COOLDOWN:
            return

        self._last = now

        threading.Thread(
            target=self._send_async,
            args=(frame.copy(), caption),
            daemon=True
        ).start()

    def _send_async(self, frame, caption):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = SNAPSHOTS / f"alert_{ts}.jpg"

        cv2.imwrite(str(path), frame)

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"

        try:
            with open(path, "rb") as img:
                requests.post(
                    url,
                    data={
                        "chat_id": TELEGRAM_CHAT,
                        "caption": f"🚨 {caption}"
                    },
                    files={"photo": img},
                    timeout=10
                )
        except Exception as e:
            print("[TELEGRAM ERROR]", e)