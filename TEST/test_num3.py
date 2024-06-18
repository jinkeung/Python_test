import pytest

#코드 정상 작동
def error():
    raise ZeroDivisionError

#코드 에러 작동
def test_error():
    with pytest.raises(ZeroDivisionError) :
        error()



def add(x,y):
    return x+y
class aaa:
    def add(x,y):
        return x+y

@pytest.fixture     #반복 수행할 함수 재활용
def Add():
    Add=aaa.add
    return Add

def test_a(Add):
    assert Add(10,5)==15
    assert Add(10,5)==15

def test_b(Add):
    assert Add(5,5)==10
    assert Add(1,5)==2
