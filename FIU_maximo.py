import random
import pyautogui
import time
import webbrowser



# Open the specified URL in the default web browser
webbrowser.open('http://mxweb.fm.fiu.edu/maximo/webclient/login/login.jsp?welcome=true')

# Wait for the browser to open and load the page
time.sleep(5)

# Write the username (6350019)
pyautogui.write('***', interval=0.1)

# Press Tab to move to the password field
pyautogui.press('tab')

# Write the password (R3mangalatuerka!)
pyautogui.write('***', interval=0.1)

# Press Enter to submit the login form
pyautogui.press('enter')

# Wait a moment for the page to load (adjust the time if needed)
time.sleep(3)

for i in range(5):
    pyautogui.click(200, 500)

    # Press space (if needed for further navigation or action)
    pyautogui.press('space')

    pyautogui.moveTo(695, 836, duration=1)
    pyautogui.click()
    time.sleep(2)

    pyautogui.moveTo(229, 216, duration=1)
    pyautogui.click()
    time.sleep(2)

    pyautogui.moveTo(81, 793, duration=1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.write('6350019', interval=0.1)

    pyautogui.moveTo(1009, 676, duration=1)
    pyautogui.click()
    pyautogui.hotkey('command', 'a')
    pyautogui.write('4', interval=0.1)

    time.sleep(1)

    pyautogui.moveTo(290, 217, duration=1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(87, 676, duration=1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(407, 657, duration=1)
    pyautogui.click()
    time.sleep(1)
    evaluations = [
    "Everything is correct",
    "Everything ok",
    "All set",
    "Done",
    "Finished with the work",
    "Task completed",
    "Work accomplished",
    "Success",
    "All done",
    "Work complete",
    "All good",
    "Everything looks good",
    "Checked and confirmed",
    "Verified and done",
    "Everything in order",
    "Execution complete",
    "No issues",
    "Correct and finished",
    "Achieved the goal",
    "Successful completion",
    "Work finalized",
    ]
    Random_evaluation = random.choice(evaluations)
    pyautogui.write(Random_evaluation, interval=0.1)

    pyautogui.moveTo(809, 175, duration=1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(926, 749, duration=1)
    pyautogui.click()
    time.sleep(3)

    pyautogui.moveTo(773, 174, duration=1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(562, 443, duration=1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(492, 529, duration=1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(934, 743, duration=1)
    pyautogui.click()
    time.sleep(4)

    pyautogui.moveTo(21, 131, duration=1)
    pyautogui.click()
    time.sleep(3)
