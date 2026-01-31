import time
import pyautogui

# Replace with your recorded coordinates
SPOT1 = (761, 230)
SPOT2 = (387, 940)
SPOT3 = (757, 752)

SPOT1_INTERVAL = 1       # seconds
POST_REFRESH_INTERVAL = 5 # seconds

REFRESH_EVERY = 0.5 * 60  # 0.5 minutes
TOTAL_CYCLES = 25

def click_spot(xy):
    pyautogui.moveTo(xy[0], xy[1], duration=0)
    pyautogui.click()

def refresh_page():
    pyautogui.hotkey("command", "r")

print("Starting in 5 seconds. Keep the browser focused and do not move it.")
time.sleep(5)

for cycle in range(1, TOTAL_CYCLES + 1):
    print(f"Cycle {cycle}/{TOTAL_CYCLES}: Spot 1 clicks every {SPOT1_INTERVAL}s for 0.5 minutes")

    # Spot 1: click every 1s until refresh time
    start = time.time()
    while time.time() - start < REFRESH_EVERY:
        click_spot(SPOT1)
        time.sleep(SPOT1_INTERVAL)

    print("Refreshing page")
    refresh_page()
    time.sleep(4)  # wait for reload

    # After refresh: click every 3s while moving through spots, then back to spot 1
    print(f"Post refresh: clicking Spot 2 every {POST_REFRESH_INTERVAL}s, then Spot 3 every {POST_REFRESH_INTERVAL}s")

    click_spot(SPOT2)
    time.sleep(POST_REFRESH_INTERVAL)

    click_spot(SPOT3)
    time.sleep(POST_REFRESH_INTERVAL)

    print("Returning to Spot 1 and resuming 1-second clicks")

print("Done.")
