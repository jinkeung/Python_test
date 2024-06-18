def text(func):
    def wrap(num):
        for i in range(num):
            print("Hello")
    return wrap

@text
def function(num):
    return num
