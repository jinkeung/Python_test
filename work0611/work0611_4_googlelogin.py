import time

import pyautogui as gui
import webbrowser

gui.prompt("aa","dd")


webbrowser.open("https://www.google.com")
time.sleep(3)
print(gui.locateOnScreen("sc.png"))
gui.click((gui.locateCenterOnScreen("sc.png"))[0],(gui.locateCenterOnScreen("sc.png"))[1])
time.sleep(2)
gui.write("jinkeung1203@gmail.com")
gui.press("enter")
time.sleep(2)
gui.write("rla10293847")
gui.press("enter")
