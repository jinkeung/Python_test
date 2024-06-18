'''
pynput, tkinter -> matplotlib [그래프]

pynput [python + input]
    #Standard input [기본적인 입력 장치: 마우스, 키보드]를 인식시키는 외부 라이브러리
    #pip install pynput

import pynput.keyboard as keyboard        #import 방식 1
#from pynput import keyboard              #       방식 2(불러온 자체가 as) == import pynput.keyboard as keyboard

keyboard.Key                              #[키보드 단축키 호출]
keyboard.KeyCode                          #[컴퓨터가 인지하는 키보드 값]
keyboard.Listener                         #[키보드의 입력값들을 인지시키는 파이썬에서 받아오는 역할]
'''

from pynput import keyboard

def ex(key):
# ascii +- 65[A] 97[a] - string
# upper, lower - string
    try:
        print(ord(key.char)) # ord 문자를 -> 숫자(아스키코드)
        print(chr(97))       # 숫자(아스키코드) -> 문자
    except AttributeError:
        print("오류")
        pass

    if key == keyboard.Key.esc:
        return False

#listner = keyboard.Listener(on_press=ex) #동작 발동 - def

#listner.start()   #해당 리스너를 boot(실행)
#listner.join()    #해당 리스너 무한루프
#listner.stop()   #해당 리스너를 off  => 메모리 소거 but join 무한루프 때문에 못읽음

#with 기능: 해당 구문을 실행하고 나서 어떠한 방식으로든 구문이 끝나면
#          메모리 소거 작업 [start(), stop()]
#           open(),thread()
#   -with 실행문 as 변수명:
#           변수명.기능



with keyboard.Listener(on_press=ex) as listener:
    listener.join()






