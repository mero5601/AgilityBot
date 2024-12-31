import pyautogui
import random
import time

# Points with a margin of ±50 pixels
points = [(2845, 505), (2866, 602)]
margin = 30

def random_click_around_points(points, margin, num_clicks):
    print(f"Performing {num_clicks} clicks:")
    for _ in range(num_clicks):
        point = random.choice(points)
        x = random.randint(point[0] - margin, point[0] + margin)
        y = random.randint(point[1] - margin, point[1] + margin)
        print(f"Clicking at ({x}, {y})...")
        pyautogui.click(x, y)
        time.sleep(1)  # 1-second delay between clicks
    print("Done!")

# Main execution
try:
    num_clicks = int(input("Enter the number of clicks to perform (default is 10): ") or 10)
    random_click_around_points(points, margin, num_clicks)
except KeyboardInterrupt:
    print("\nProgram stopped.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
