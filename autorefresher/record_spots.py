from pynput import keyboard
import pyautogui

spots = []

print("Hover over a spot and press F8 to record it.")
print("Press Esc when finished.\n")

def on_press(key):
    if key == keyboard.Key.f8:
        pos = pyautogui.position()
        spots.append(pos)
        print(f"Recorded spot {len(spots)}: {pos}")
    elif key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

print("\nFinal spots list:")
for i, s in enumerate(spots, start=1):
    print(f"SPOT{i} = {s}")
