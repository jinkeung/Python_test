import time

import pyautogui as gui
import webbrowser


webbrowser.open("https://www.google.com")
time.sleep(1)

id=gui.prompt("아이디 입력","제목")
pw=gui.password("패스워드 입력","제목")

time.sleep(1)
print(gui.locateOnScreen("sc.png"))
gui.click((gui.locateCenterOnScreen("sc.png"))[0],(gui.locateCenterOnScreen("sc.png"))[1])
time.sleep(2)
gui.write(id)
gui.press("enter")
time.sleep(2)
gui.write(pw)
gui.press("enter")


import pyinstall
