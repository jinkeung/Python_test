
def answer(func):
    def add(*args, **kwargs):
        print(sum(func(*args, **kwargs)))
    return add

@answer
def function1(num):
    return range(1,num+1)

function1(5)
function1(10)

@answer
def function2(num):
    return range(2,num+2)

function2(5)
function2(10)