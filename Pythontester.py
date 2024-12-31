from pynput.mouse import Listener, Button
from datetime import datetime

# Function to handle mouse clicks
def on_click(x, y, button, pressed):
    current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]  # Format to include hours, minutes, seconds, and milliseconds

    if pressed:
        if button == Button.left:
            print(f"Left Click at position ({x}, {y}) at {current_time}")
        elif button == Button.right:
            print(f"Right Click at position ({x}, {y}) at {current_time}")
        elif button == Button.middle:
            print(f"Middle Click (pressed) at position ({x}, {y}) at {current_time}")
    else:
        if button == Button.left:
            print(f"Left Click released at position ({x}, {y}) at {current_time}")
        elif button == Button.right:
            print(f"Right Click released at position ({x}, {y}) at {current_time}")
        elif button == Button.middle:
            print(f"Middle Click released at position ({x}, {y}) at {current_time}")

# Listener setup
with Listener(on_click=on_click) as listener:
    print("Tracking mouse clicks. Press Ctrl+C to stop.")
    listener.join()
