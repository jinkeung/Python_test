'''
#파이썬: 객체지향언어 -다양성, 캡슐화

#def
#class

#os
#pyinstaller

#pytest
#decorator
#@wrap

'''

'''
#class, def
class sound:                #클래스

    def __init__(self):     #생성자
        print("init")

    def func():             #메소드 함수
        return __name__

if __name__ == '__main__':
    print(sound.func())

print(sound.func())
'''






'''
#decorator 파이썬 데코레이터
    #구조 -함수가 함수 호출
          인수 전달 - 변수명이 없는 변수
          *args : 리스트 정보 전달
          **kwargs : 딕셔너리 정보 전달
    1. 함수의 코드 유연성-기존 함수를 망가뜨리지 않고 새롭게 쓸 수 있다.
    2. 코드의 캡슐화
    3. 인수의 전달
'''

def decorator(func):
    def wrap():
        print("Hello")
        func()
        print("World")

def function():
    print("Hello")



'''
def wrap(*args):
    print(args)

wrap([1,2,3,4])

def wrap2(**kwargs):
    print(kwargs)
wrap2(A="Hello",B="World")

def wrap3(*args,**kwargs):
    print(args)
    print(kwargs)

wrap3(1,2,3,4,A="Hello",B="World")
'''
'''
def test1(a):
    a()
    print("World")

def function(name):
    print(name)

#test1(function("NAME"))   인수전달이 안됨 a() 안쪽에
'''


'''
#코드의 유연성 예시(데코레이터는 아님)
test=function       #변수에 함수도 들어감
test()

def test1(func):
    func()
    print("WORLD")

def function():
    print("HELLO")

test1(function)
'''
