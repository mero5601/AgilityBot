import pyautogui
import time
import random

# Define positions as pairs
position_pairs = [
    [(3082, 518), (2656, 583)],  # Pair 1 (odd, even)
]

print("Starting to randomly alternate clicks within ±10 pixel variation. Press CTRL+C to stop.")

try:
    while True:
        # Randomly choose a pair of positions (odd and even)
        chosen_pair = random.choice(position_pairs)

        for position in chosen_pair:
            # Add random ±10 pixel variation to both x and y coordinates
            x, y = position
            x += random.randint(-10, 10)
            y += random.randint(-10, 10)

            # Move the mouse to the new position
            pyautogui.moveTo(x, y)
            print(f"Moved to ({x}, {y})")

            # Click at the position
            pyautogui.click(x, y)
            print(f"Clicked at ({x}, {y})")

            # Randomized delay between 3.0 and 4.2 seconds
            delay = random.uniform(3.0, 4.2)
            print(f"Waiting for {delay:.2f} seconds...")
            time.sleep(delay)
except KeyboardInterrupt:
    print("Script stopped by user.")
