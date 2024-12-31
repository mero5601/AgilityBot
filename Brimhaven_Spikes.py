import pyautogui
import time

# Define positions to click
positions = [
    (927, 574),
    (734, 480),
    (915, 608),
    (720, 466),
    (918, 592),
    (733, 466),
    (906, 592),
    (742, 477),
    (910, 588),
    (738, 477)
]

print("Starting to alternate clicks. Press CTRL+C to stop.")

try:
    while True:
        for position in positions:
            # Move the mouse to the position first
            pyautogui.moveTo(position)
            print(f"Moved to {position}")
            
            # Click at the position
            pyautogui.click(position)
            print(f"Clicked at {position}")
            
            # Wait for the specified time (3.1 or 3.2 seconds)
            time.sleep(3.2)
except KeyboardInterrupt:
    print("Script stopped by user.")
