import time
import pyautogui

CLICK_INTERVAL_SECONDS = 0.5 * 60  # 30 seconds

print("Autoclicker started. Press Ctrl+C to stop.")

while True:
    pyautogui.click()
    print("Clicked at", time.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(CLICK_INTERVAL_SECONDS)
