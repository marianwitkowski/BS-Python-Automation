
# lokalizacja myszy
import pyautogui
import time

def detect_mouse():
    while True:
        curr_x, curr_y = pyautogui.position()
        print(curr_x, curr_y)
        time.sleep(1.5)

detect_mouse()