from flask import Flask
import cv2
import time
from datetime import datetime
import os

app = Flask(__name__)

SAVE_DIR = "captures"
os.makedirs(SAVE_DIR, exist_ok=True)

@app.route('/detect', methods=['POST'])
def detect():
    print("📡 DETECT received from ESP32")

    cam = cv2.VideoCapture(0)
    time.sleep(1)
    ret, frame = cam.read()
    cam.release()

    if not ret:
        print("❌ Camera capture failed")
        return "Camera Error", 500

    filename = f"capture_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
    path = os.path.join(SAVE_DIR, filename)

    cv2.imwrite(path, frame)
    print(f"✅ Image saved at: {path}")

    return "OK", 200


if __name__ == "__main__":
    print("🚀 Server running...")
    app.run(host="0.0.0.0", port=5000)
