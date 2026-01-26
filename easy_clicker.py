import time
import threading
import pyautogui
import sys

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
GRAY = "\033[90m"
YELLOW = "\033[93m"
RESET = "\033[0m"

running = False
stop_event = threading.Event()

interval_seconds = 30  # default: 30 seconds
seconds_remaining = interval_seconds

lock = threading.Lock()

def beep():
    sys.stdout.write("\a")
    sys.stdout.flush()

def click_loop():
    global seconds_remaining

    while not stop_event.is_set():
        try:
            pyautogui.click()
            beep()
        except Exception:
            pass

        with lock:
            seconds_remaining = int(interval_seconds)

        while True:
            time.sleep(1)
            with lock:
                if stop_event.is_set():
                    return
                seconds_remaining -= 1
                if seconds_remaining <= 0:
                    break

def status_loop():
    while True:
        with lock:
            is_running = running
            remaining = seconds_remaining
            interval = interval_seconds

        if is_running:
            status = (
                f"{GREEN}Status: RUNNING{RESET} {GRAY}|{RESET} "
                f"Next click in: {YELLOW}{remaining}s{RESET} {GRAY}|{RESET} "
                f"Interval: {YELLOW}{interval}s{RESET}"
            )
        else:
            status = (
                f"{RED}Status: STOPPED{RESET} {GRAY}|{RESET} "
                f"Interval: {YELLOW}{interval}s{RESET} {GRAY}|{RESET} "
                f"Type seconds + ENTER, or press ENTER to start"
            )

        sys.stdout.write("\r" + status + " " * 10)
        sys.stdout.flush()
        time.sleep(1)

def start_clicker():
    global running, seconds_remaining
    with lock:
        if running:
            return
        running = True
        stop_event.clear()
        seconds_remaining = int(interval_seconds)
    threading.Thread(target=click_loop, daemon=True).start()

def stop_clicker():
    global running, seconds_remaining
    with lock:
        if not running:
            return
        running = False
        stop_event.set()
        seconds_remaining = int(interval_seconds)

def set_interval(new_seconds):
    global interval_seconds, seconds_remaining
    if new_seconds <= 0:
        return False
    with lock:
        interval_seconds = int(new_seconds)
        seconds_remaining = interval_seconds
    return True

def input_loop():
    print("\nAUT0CLICKER")
    print("ENTER = start / stop")
    print("Type number of SECONDS + ENTER to change interval")
    print("Type q + ENTER to quit\n")

    try:
        while True:
            user = input().strip().lower()

            if user == "":
                with lock:
                    is_running = running
                if is_running:
                    stop_clicker()
                else:
                    start_clicker()
                continue

            if user in {"q", "quit", "exit"}:
                stop_clicker()
                print("\nExited")
                return

            try:
                secs = int(user)
                if not set_interval(secs):
                    print("\nInterval must be > 0 seconds.")
            except ValueError:
                print("\nInvalid input. Press ENTER, type seconds, or q.")

    except KeyboardInterrupt:
        stop_clicker()
        print("\nExited")

if __name__ == "__main__":
    threading.Thread(target=status_loop, daemon=True).start()
    input_loop()
