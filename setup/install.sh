#!/bin/bash
set -e
echo "=== Smart Surveillance — Setup ==="

python3 -m venv venv
source venv/bin/activate


pip install -r setup/requirements.txt

# Pre-download YOLOv8 nano weights
python3 -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"

# Create data directories
mkdir -p data/snapshots models/trained

# Test camera
python3 -c "
import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print('Camera OK:', ret, '| Resolution:', frame.shape if ret else 'FAILED')
cap.release()
"

echo ""
echo "=== Setup complete! ==="
echo "Next: fill in config/.env with your Telegram token"
echo "Then run: python main.py --scenario railway"