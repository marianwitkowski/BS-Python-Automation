import pyautogui
import time
import subprocess

subprocess.Popen(r"c:\windows\system32\mspaint.exe")
time.sleep(2)

# maksymalizacja okna
pyautogui.hotkey("win","up")
time.sleep(2)

# wybor narzedzia do malowania
pyautogui.click(x=476, y=65)
time.sleep(1)

# narysuj prostokat
pyautogui.moveTo(x=200, y=300)
pyautogui.dragTo(x=300, y=400, duration=1)
time.sleep(3)

pyautogui.hotkey("alt","f4")
pyautogui.press("right")
time.sleep(3)
pyautogui.press("enter")