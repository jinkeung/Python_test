class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hello(self):
        print(f"HI, my name is {self.name}. I am {self.age} years old." )

    def more(self):
        print("one more!")
        self.say_hello()

