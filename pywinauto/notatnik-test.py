from pywinauto import keyboard
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time

app = Application().connect(path=r"c:\windows\system32\notepad.exe")
items = app.windows()
print(items)
dlg = app['Bez tytułu — Notatnik']
dlg.print_control_identifiers()

dlg.Edit.type_keys("Linia{SPACE}tekstu")
dlg.set_focus()
keyboard.send_keys("1..2.3..4")

dlg.menu_select("Plik -> Zapisz jako...")
send_keys("c:\\tmp\\test2.txt{ENTER}")

send_keys("{LEFT}{ENTER}")

