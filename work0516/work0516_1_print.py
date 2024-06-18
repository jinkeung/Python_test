print("Hello")          #print문 default:  end="\n"(개행) sep=""(구분자 없음)
                        #end: 해당 구문이 완료 되었을 때, sep: 해당 구문이 구분 되었을 때만 출력
print("Hello",end="")
print("World")
print("%3d Won" %10)

num1=10
num2=20
num3=10.5


print(num1,num2)                    #10 20
print(str(num1)+str(num2))          #1020

print("%d %d" % (num1,num2))        #10 20

print(num1,num2,sep=",")            #10,20

print("num1 type: ",type(num1))     #int
print("num3 type: ",type(num3))     #float


import math

print(3**3)
math.pow(3,3)

text1='A'
text2="A"

print("text1 type: ",type(text1))      #str
print("text2 type: ",type(text2))      #str

print("'Hello'")    #'Hello'
print('"Hello"')    #"Hello"
print("""
line1
line2
line3""")


print(text1*5)      #AAAAA (문자 반복)
print(text1+text2)  #AA (concat)

text3="ABCD"
print(text3[0:2])  #AB

text4="ABAD"
print(text4.index("A")) #0

