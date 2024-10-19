import pyautogui
import time
import webbrowser
import random
import pytesseract
from PIL import ImageGrab


time.sleep(2)
# Open Google in the default web browser
webbrowser.open('https://www.google.com')

# Wait for the browser to open and load Google (adjust the time if necessary)
time.sleep(5)

# Type 'ChatGPT' in the search bar
pyautogui.write('ChatGPT', interval=0.1)

# Press 'Enter' to search
pyautogui.press('enter')

# Wait for the search results to load
time.sleep(5)

# Move the mouse to the ChatGPT link position on the Google results page (get the position manually)
# Example: Replace (x, y) with the actual coordinates of the ChatGPT link
pyautogui.moveTo(2775, 705 )  # Adjust these coordinates based on your screen
pyautogui.click()


# Wait for ChatGPT page to load (adjust based on your connection speed)
time.sleep(4)

# Move to the ChatGPT input field (get the position manually)
# Example: Replace (x, y) with the actual coordinates of the input box on ChatGPT's page
pyautogui.moveTo(3280, 545)  # Adjust these coordinates based on your screen
pyautogui.click()

# Define a list of random questions to ask ChatGPT
random_questions = [
    "What is the capital of France?",
    "How do you write a Python script?",
    "Tell me a joke.",
    "What is machine learning?",
    "Who won the last World Cup?"
]

# Choose a random question
question = random.choice(random_questions)

# Type the random question into the ChatGPT input box
pyautogui.write(question, interval=0.1)

# Press 'Enter' to submit the question
pyautogui.press('enter')
time.sleep(15)

# Take a screenshot of the screen
screenshot = ImageGrab.grab()

# Use pytesseract to extract text from the screenshot
text_data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)

# The word you want to find
target_word = "CJ GPT Django"

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