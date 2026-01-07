import serial
import time
import cv2
from datetime import datetime
import subprocess
import os

# --- Serial Port Setup ---
ser = serial.Serial('COM8', 115200, timeout=1)
time.sleep(2)

print("Listening for ESP32 trigger...")

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        print("Received:", line)

        if "DETECT" in line:
            print("Trigger received! Capturing image...")

            # Capture from webcam
            cam = cv2.VideoCapture(0)
            time.sleep(1)
            ret, frame = cam.read()

            if ret:
                filename = f"capture_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
                full_path = os.path.abspath(filename)
                cv2.imwrite(full_path, frame)
                print(f"✅ Image saved as {full_path}")

                # Open Bluetooth File Transfer window (manual)
                print("📤 Opening Bluetooth file transfer window...")
                subprocess.run("start fsquirt", shell=True)
                print("➡️ Choose 'Send files' and select the image.")
            else:
                print("⚠️ Camera error: could not capture image")

            cam.release()
            cv2.destroyAllWindows()
