import time
import random
from pynput.mouse import Controller, Button

# Initialize the mouse controller
mouse_controller = Controller()

# Function to simulate a click at a position
def simulate_click(position, button=Button.left):
    mouse_controller.position = position
    mouse_controller.press(button)
    print(f"Clicked at {position}")
    mouse_controller.release(button)

# Function to simulate a middle mouse press and release with slow, human-like movement
def simulate_middle_click(press_position, release_position, hold_duration):
    mouse_controller.position = press_position
    mouse_controller.press(Button.middle)
    print(f"Middle click pressed at {press_position}")

    # Simulate slow movement from press to release
    smooth_move(press_position, release_position)

    # Simulate hold duration
    time.sleep(hold_duration)

    mouse_controller.release(Button.middle)
    print(f"Middle click released at {release_position}")

# Function to simulate slow, smooth mouse movement between two points
def smooth_move(start_pos, end_pos, steps=20, delay=0.05):
    x1, y1 = start_pos
    x2, y2 = end_pos

    print(f"Moving mouse from {start_pos} to {end_pos} in {steps} steps...")

    for step in range(steps):
        # Calculate intermediate positions
        x = int(x1 + (x2 - x1) * (step / float(steps)))
        y = int(y1 + (y2 - y1) * (step / float(steps)))

        # Add small random noise to make the movement feel more human-like
        x += random.randint(-5, 5)
        y += random.randint(-5, 5)

        # Move the mouse to the intermediate position
        mouse_controller.position = (x, y)
        
        # Print debug information
        print(f"Step {step + 1}: Moving to ({x}, {y})")

        # Sleep for a short time to simulate a slower movement
        time.sleep(delay)

# Function to execute the sequence of actions
def execute_sequence(sequence):
    t = 0  # Virtual clock starts at 0

    for action in sequence:
        delay = action["time"] - t
        t += delay

        # Execute the action
        if action["type"] == "click":
            simulate_click(action["position"])
        elif action["type"] == "middle_click":
            simulate_middle_click(action["press"], action["release"], action["hold"])

# Define the sequence of actions
def main():
    sequence = [
        
        {"type": "click", "position": (1557, 184), "time": 500},
        {"type": "click", "position": (1527, 175), "time": 500},
        {"type": "click", "position": (1489, 112), "time": 500},
        {"type": "click", "position": (1491, 137), "time": 500},
        {"type": "click", "position": (1003, 281), "time": 500},
        {"type": "click", "position": (1497, 141), "time": 500},
        {"type": "click", "position": (978, 660), "time": 500},
        
        
    
    ]

    execute_sequence(sequence)

if __name__ == "__main__":
    main()
