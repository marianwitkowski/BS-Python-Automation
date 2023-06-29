
# interakcja z Notatnikiem
import pyautogui
import time

# otworz Notatnik
pyautogui.hotkey("win", "r")
time.sleep(2)

pyautogui.write(r"c:\windows\notepad.exe")
pyautogui.press("enter")
time.sleep(2)

pyautogui.press('alt')
pyautogui.press('m')
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('esc')

pyautogui.alert("Zaraz zostanie wprowadzony tekst")

# wpisywanie tekstu
pyautogui.write("Linia numer 1 tekstu")
pyautogui.press("enter")
pyautogui.write("Linia numer 2 tekstu")
pyautogui.press("enter")
pyautogui.typewrite("Linia numer 3\nLinia nr 4\n", interval=0.1)

# prosba o podanie tekstu
txt = pyautogui.prompt("Prosze podac tekst:")
pyautogui.write(txt)

# zapis pliku
pyautogui.hotkey("ctrl","s") # Zapisz jako...
time.sleep(1)
pyautogui.write(r"c:\tmp\plik1.txt")
time.sleep(2)

# zamknij aplikacje
pyautogui.hotkey("alt", "f4")


