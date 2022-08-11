import pyautogui, time

position = pyautogui.position ()
message = "test"
for a in range(5):
    pyautogui.click(position.x, position.y)
    pyautogui.typewrite(message)
    print(message)
    time.sleep(0.5)
    pyautogui.typewrite(["enter"])