import pyautogui
import pytesseract
from PIL import ImageGrab
import time

# Set the path to tesseract executable if required (Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Wait for a few seconds before the script starts
time.sleep(2)

# Take a screenshot of the screen
screenshot = ImageGrab.grab()

# Use pytesseract to extract text from the screenshot
text_data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)

# The word you want to find
target_word = "Terminal"

# Iterate over the words detected by Tesseract
for i, word in enumerate(text_data['text']):
    if target_word in word:
        # Get the coordinates of the word on the screen
        x = text_data['left'][i]
        y = text_data['top'][i]
        width = text_data['width'][i]
        height = text_data['height'][i]

        # Calculate the center of the word's bounding box
        center_x = x + width // 2
        center_y = y + height // 2

        # Move the mouse to the center of the word and click
        pyautogui.moveTo(center_x, center_y)
        pyautogui.click()

        print(f"Clicked on '{target_word}' at ({center_x}, {center_y})")
        break
else:
    print(f"'{target_word}' not found on the screen.")
