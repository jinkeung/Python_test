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

def num():
    return 0.8

def test_num():
    assert num()==0.7


def test_num2():
    assert num()>=0.7

