# Autoclicker (macOS)

A simple, reliable autoclicker for macOS with a live status display.

No GUI. No setup complexity. One key to start or stop.

---

## What this does

- Clicks wherever your mouse cursor is
- Runs at a configurable interval in seconds
- Shows live status in the terminal:
  - RUNNING or STOPPED
  - Countdown until next click
- Beeps every time a click happens

---

## Requirements

- macOS
- Python 3 installed
- Terminal access

---

## One time setup

### 1. Install Python dependency

Open Terminal and run:

```bash
pip3 install pyautogui


If it says “already satisfied”, you are good.

2. macOS permission

The first time it clicks, macOS may block it.

If clicks do not happen:

Open System Settings

Go to Privacy & Security

Click Accessibility

Enable your Terminal app

Restart Terminal

This only needs to be done once.

How to run

From the project folder:

python3 clicker.py


You will see a live status line.

Controls

ENTER
Start or stop the clicker

Type a number then ENTER
Change the interval in seconds
Example: typing 30 sets it to click every 30 seconds

q + ENTER
Quit the program

CTRL + C
Force quit at any time

Example usage
Status: RUNNING | Next click in: 12s | Interval: 30s


Green means running.
Red means stopped.

Notes

Clicks happen at the current mouse position

Move your mouse before starting to change the target

Leave the terminal window open while running