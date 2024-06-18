import random

import pytest   #pip install pytest

"""
    #Pytest Framework
     TDD[Test Driven Development]
        : 개발 도중 테스트와 병행 개발
        
    구조 -구현 공간과 테스트(test) 공간 폴더로 구분
      └구현 공간
      └테스트 공간 - 테스트 파일[test_num.py]     # 어떤 테스트를 하는지 알수있게 명시~
                        └def test_*           #무조건 이름이 test_로 시작해야지 테스트 됨
        - 실행은 터미널에서해야 모든 테스트 실행 가능
          pytest test_num.py 
"""
'''
def num():
    return 0.8

def repeat(n):
    def deco(func):
        def wrap(*args, **kwargs):
            for _ in range(n):              #i가 필요없고 반복만하면될때
                func(*args, **kwargs)
        return wrap
    return deco
'''
'''
a=10

@repeat(10)                 # repeat에 10을 넣어버리고 그다음 def인 deco에 test_num이 들어감
def test_num():
    global a
    a-=1
    assert num()<=a         #실패하는순간 더이상 반복 X
'''


#병렬 실행      => 범위내에 몇개 성공 몇개실행

@pytest.mark.parametrize("key",range(1,10))

def test_num(key):
    assert key>=5