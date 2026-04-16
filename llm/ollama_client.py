import base64
import requests
import cv2
from config.settings import LLM_MODEL

OLLAMA_URL = "http://localhost:11434/api/generate"

def frame_to_b64(frame):
    _, buf = cv2.imencode(".jpg", frame)
    return base64.b64encode(buf).decode()

def describe_scene(frame):
    b64 = frame_to_b64(frame)

    prompt = "Describe what is happening in this security camera image."

    try:
        res = requests.post(OLLAMA_URL, json={
            "model": LLM_MODEL,
            "prompt": prompt,
            "images": [b64],
            "stream": False
        }, timeout=20)

        return res.json().get("response", "")
    except Exception as e:
        return f"LLM error: {e}"