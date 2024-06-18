import time

import pyautogui as gui
import webbrowser

webbrowser.open("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EB%89%B4%EC%8A%A4")
time.sleep(2)
gui.scroll(-100)

gui.alert("Hello","title","confirm")
id=gui.prompt("아이디 입력","제목")
pw=gui.password("패스워드 입력","제목")
bool_text=gui.confirm()
print(id)
print(pw)
