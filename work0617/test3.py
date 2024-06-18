
def sum(func):
    def wrap(*args,**kwargs):
        sum_num=0
        for i in func(*args,**kwargs):
            sum_num+=i
        print(sum_num)
        return func
    return wrap

@sum
def function(*args):
    return args
function(1,2,3,4,5)
