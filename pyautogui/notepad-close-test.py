# interakcja z Notatnikiem
import pyautogui
import time

# otworz Notatnik
pyautogui.hotkey("win", "r")
time.sleep(2)

pyautogui.write(r"c:\windows\notepad.exe")
pyautogui.press("enter")
time.sleep(5)

# zamknij aplikacje
pyautogui.hotkey("alt", "f4")

