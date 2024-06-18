
def repeat(n):
    def deco(func):
        def wrap(*args, **kwargs):
            for _ in range(n):              #i가 필요없고 반복만하면될때
                func(*args, **kwargs)
        return wrap
    return deco

def text():
    return "Hello"



def test_text():
    assert 'e' in text()
    assert 'a' in text()
