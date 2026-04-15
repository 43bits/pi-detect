import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ── Paths ──────────────────────────────────────────────────
BASE_DIR     = Path(__file__).parent.parent
MODELS_DIR   = BASE_DIR / "models"
FACES_DIR    = MODELS_DIR / "faces"
DATA_DIR     = BASE_DIR / "data"
SNAPSHOTS    = DATA_DIR / "snapshots"
PATH_LOGS    = DATA_DIR / "path_logs"
DB_PATH      = DATA_DIR / "events.db"

# ── Camera ─────────────────────────────────────────────────
CAMERA_INDEX    = 0           # 0=laptop webcam, 1=external, "http://...=IP cam"
FRAME_WIDTH     = 1280
FRAME_HEIGHT    = 720
FRAME_BUFFER    = 5           # frames to buffer before processing

# ── Detection ──────────────────────────────────────────────
YOLO_MODEL      = str(MODELS_DIR / "yolov8n.pt")
YOLO_CONF       = 0.5
YOLO_CLASSES    = [0]         # 0 = person

# ── Alerts ─────────────────────────────────────────────────
ALERT_COOLDOWN       = 5       # seconds between voice alerts
TELEGRAM_COOLDOWN    = 15      # seconds between Telegram messages
LOITER_SECONDS       = 8       # dwell time before loitering alert

# ── Telegram ───────────────────────────────────────────────
TELEGRAM_TOKEN  = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT   = os.getenv("TELEGRAM_CHAT_ID", "")

# ── LLM ────────────────────────────────────────────────────
LLM_MODEL       = "llava"     # or "phi3", "moondream"
LLM_ENABLED     = True
LLM_QUERY_EVERY = 30          # query LLM every N seconds

# ── Night mode ─────────────────────────────────────────────
NIGHT_MODE_AUTO   = True
BRIGHTNESS_THRESH = 60        # pixel mean below this = night mode on