import pyautogui
import time

mouseclick=pyautogui

# Perform 5 clicks
for i in range(10):
    print(f"Click {i + 1} at position {pyautogui.position()}")  # Diagnostic output
    pyautogui.click()  # Perform a left click
    time.sleep(4)  # Delay of 1 second

print("Finished mouse clicks.")
