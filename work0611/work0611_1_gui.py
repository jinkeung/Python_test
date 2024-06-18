import pyautogui as gui
#키보드, 마우스, 위치값 판단 작업 외부라이브러리

gui.size()
print(gui.size())           #모니터 디스플레이 해상도
print(gui.position())       #마우스 기준으로 x,y 출력

'''
#마우스
gui.move(100,100)           #상대적 위치 이동(현재 위치를 기준으로) ==moveRel
gui.moveTo(100,100)         #절대적 위치 이동(좌표)
gui.move(100,100,duration=1)


print(gui.size().width)
gui.moveTo((gui.size().width)/2,(gui.size().height)/2)

gui.click(10,10,button="left",clicks=2,interval=0.3)
gui.move(100,100,duration=5)

gui.drag(100,100,duration=3)        #상대적 위치 까지 드래그
gui.dragTo(100,100,duration=3)      #절대적 위치만큼 드래그

gui.mouseInfo()
'''
'''
gui.keyDown("ctrl")                 #키보드 계속 누르고 있음
gui.keyDown("c")
gui.keyUp("c")                      #키보드 떼기
gui.keyUp("ctrl")

gui.hotkey("ctrl", "c")        #단축키

print(gui.KEYBOARD_KEYS)
gui.press("a")                  #keyDown+keyUp

gui.write("Hello")
gui.typewrite("Hello",interval=0.1)
'''

import pyperclip
#클립보드 기능 적용, 구현하는 외부 라이브러리
text="안녕하세요"
pyperclip.copy(text)
print(pyperclip.paste())

