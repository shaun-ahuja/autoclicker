import time
import threading
import sys
import pyautogui
from pynput import keyboard

# =========================
# CONFIG
# =========================

SPOT1 = (761, 230)
SPOT2 = (387, 940)
SPOT3 = (757, 752)

SPOT1_INTERVAL = 1         # seconds
POST_REFRESH_INTERVAL = 10  # seconds
POST_REFRESH_DELAY = 10    # seconds before clicking Spot 2

REFRESH_EVERY = 19 * 60    # 19 minutes
TOTAL_CYCLES = 30

# =========================
# GLOBAL STOP FLAG
# =========================

stop_program = False

# =========================
# KILL SWITCH
# Command + Shift + K
# =========================

def start_kill_switch():
    current_keys = set()

    def on_press(key):
        global stop_program
        current_keys.add(key)

        if (
            keyboard.Key.cmd in current_keys
            and keyboard.Key.shift in current_keys
            and isinstance(key, keyboard.KeyCode)
            and key.char == "k"
        ):
            print("\nKill switch activated. Exiting now.")
            stop_program = True
            sys.exit(0)

    def on_release(key):
        current_keys.discard(key)

    with keyboard.Listener(on_press=on_press, on_release=on_release):
        while True:
            time.sleep(0.1)

# =========================
# HELPERS
# =========================

def click_spot(xy):
    if stop_program:
        sys.exit(0)
    pyautogui.moveTo(xy[0], xy[1], duration=0)
    pyautogui.click()

def refresh_page():
    if stop_program:
        sys.exit(0)
    pyautogui.hotkey("command", "r")

# =========================
# START
# =========================

print("Starting in 5 seconds.")
print("Kill switch hotkey: Command + Shift + K")
time.sleep(5)

kill_thread = threading.Thread(target=start_kill_switch, daemon=True)
kill_thread.start()

for cycle in range(1, TOTAL_CYCLES + 1):
    if stop_program:
        break

    print(f"Cycle {cycle}/{TOTAL_CYCLES}: Spot 1 clicking every {SPOT1_INTERVAL}s")

    start_time = time.time()
    while time.time() - start_time < REFRESH_EVERY:
        click_spot(SPOT1)
        time.sleep(SPOT1_INTERVAL)

    print("Refreshing page")
    refresh_page()
    time.sleep(POST_REFRESH_DELAY)

    print("Post refresh clicks")

    click_spot(SPOT2)
    time.sleep(POST_REFRESH_INTERVAL)

    click_spot(SPOT3)
    time.sleep(POST_REFRESH_INTERVAL)

    print("Returning to Spot 1")

print("Automation finished.")
