def answer(func):
    def deco_answer(*args, **kwargs):
        print(f"{func.__name__}시작")
        print(*args, **kwargs)
        print(func(*args, **kwargs))
    return deco_answer

@answer
def add(a,b):
    return a+b

@answer
def subtract(a,b):
    return a-b
@answer
def multiply(a,b):
    return a*b
@answer
def divide(a,b):
    return a/b

add(4,2)
subtract(4,2)
multiply(4,2)
divide(4,2)