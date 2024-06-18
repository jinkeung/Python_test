import time

import pyautogui as gui
import webbrowser

webbrowser.open("https://www.google.com/")

gui.click(1450,200,clicks=2,interval=2)
gui.write("jinkeung1203@gmail.com")
gui.press("Enter")
gui.click(900,550,clicks=2,interval=2)
gui.write("rla10293847")
gui.press("Enter")

#time.sleep(2)   #시간 멈춤