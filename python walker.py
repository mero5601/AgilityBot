import time
import random
from pynput.mouse import Controller, Button

# Initialize the mouse controller
mouse_controller = Controller()

# Function to simulate the middle button press and release with slow, human-like camera swing
def simulate_click():
    # Coordinates to simulate the click and release
    # move camera from bank 18:36:06.273 --> 18:36:07.236
    press_position1 = (1173, 380) 
    release_position1 = (1440, 356)

    #standard left click, release not important 18:37:33.714
    press_position2=(1205,104)
   
   #third click to get to agility obstacle, no RNG allowed on this click 18:38:31.224
   press_position3=(1630,127)

    #center compas, allow +- 40 pixels 18:40:30.608
    press_position4=(1481,51)


    #agility obstacle 18:43:21.985
    press_position5=(1290,764)



    #change camera, middle click 18:45:45.131 --> released at 18:47:45.59
    press_position6=(1259,499)
    release_position6=(1764,486)
    #enter rune 18:47:06.680
    press_position7=(1112, 188)
    
    #minimap click 18:47:40.045
    press_position6=(1493, 115)
    
    #runecrafting sequence
Left Click at position (2679, 928) at 18:47:44.419
Left Click released at position (2572, 925) at 18:47:45.590
Left Click at position (2676, 929) at 18:47:47.037
Left Click released at position (2560, 929) at 18:47:48.348
Left Click at position (2697, 602) at 18:47:51.304
Left Click released at position (2592, 601) at 18:47:52.157
Left Click at position (2735, 551) at 18:47:53.510
Left Click released at position (2735, 551) at 18:47:53.624
Left Click at position (2741, 518) at 18:47:55.086
Left Click released at position (2415, 525) at 18:47:56.137
Left Click at position (2735, 567) at 18:48:03.384
Left Click released at position (2416, 574) at 18:48:04.550
Left Click at position (2729, 572) at 18:48:06.833
Left Click released at position (2430, 573) at 18:48:07.911
Left Click at position (1150, 492) at 18:48:13.776
Left Click released at position (1150, 492) at 18:48:13.865
Left Click at position (1464, 757) at 18:48:15.839
Left Click released at position (1464, 757) at 18:48:15.911
Left Click at position (1502, 755) at 18:48:16.254
Left Click released at position (1502, 755) at 18:48:16.343
Left Click at position (1535, 753) at 18:48:16.979
Left Click released at position (1535, 753) at 18:48:17.075
Left Click at position (1200, 485) at 18:48:18.452
Left Click released at position (1200, 485) at 18:48:18.540
Left Click at position (1587, 753) at 18:48:19.692
Left Click released at position (1587, 753) at 18:48:19.775
Left Click at position (1188, 485) at 18:48:21.220
Left Click released at position (1188, 485) at 18:48:21.319
    #minimap click 18:49:54.845
    press_position6=(1479, 41) 
    
    #portal click 18:50:10.071
    press_position6=(1300, 244)
    #agility click can go 1 tile up or down (meaning alot of leeway on this click alllowed) 18:50:41.955
    press_position6=(1174, 244)
    #use poll 18:51:55 
    press_position6=(1066, 102)
    #use bank before reaching poll  18:52:17.824
    press_position6=(926, 373) 


          

    # Print the time and position of the button press
    print(f"Simulating press at {press_position}")
    mouse_controller.position = press_position  # Move mouse to the press position
    mouse_controller.press(Button.middle)  # Press the middle button

    # Slow and random camera swing from press position to release position
    smooth_move(press_position, release_position)

    # Print the time and position of the button release
    print(f"Simulating release at {release_position}")
    mouse_controller.release(Button.middle)  # Release the middle button

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

# Run the simulation
simulate_click()
