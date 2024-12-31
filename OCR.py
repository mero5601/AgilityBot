# screenshot_detector.py
import pyautogui
import pytesseract
from PIL import Image
import sys

# Ensure Tesseract is installed and in the system PATH
# If not, you can specify the path like this:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Check if arguments are passed correctly
if len(sys.argv) != 3:
    print("Error: Please provide both x and y coordinates as arguments.")
    sys.exit(1)  # Exit if arguments are not correct

# Get the position from the command line arguments
try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
except ValueError:
    print("Error: Coordinates must be integers.")
    sys.exit(1)

# Function to capture screenshot and perform OCR
def capture_and_detect_text(x, y):
    # Take screenshot of the area around the click
    screenshot = pyautogui.screenshot(region=(x - 50, y - 50, 100, 100))  # 100x100 area around the click
    screenshot.save("screenshot.png")  # Save the screenshot (optional)
    # Perform OCR to detect text in the screenshot
    text = pytesseract.image_to_string(screenshot)
    print(f"Text in the clicked area: {text}")

# Call the function
capture_and_detect_text(2256, 202)
