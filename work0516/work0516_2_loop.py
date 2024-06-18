"""
<<반복문-for문>>
for문 - 파이썬의 배열 반복문

for 변수 in 여러값
    : 실행문
-in 연산자: 우측의 값들을 좌측에 대입하면서 True, False를 발생
-range 연산자: 지정된 숫자만큼 나열 함수
"""

for i in range(5):          #0부터 4까지(5 전까지)
    print(i, end=" ")
print()
for i in range(1,5):        #1부터 4까지(5 전까지)
    print(i, end=" ")

print()
for i in range(1,10,2):     #1부터 9까지 +2
    print(i, end=" ")
print()
for i in range(10,1,-2):    #10부터 2까지 -2
    print(i, end=" ")
print()
arr=[1,2,3,4,5]
for i in arr:               #in 우측(arr)에 있는 값들을 좌측(i)에 대입
    print(i, end=" ")
print()
"""
<<반복문-while문>>
while문-조건에 부합하면 반복, break, continue 사용 가능 

while 조건:
    실행문
"""
num=1
while (num<=10):
    print(num, end=" ")
    num+=1

text="ABC"
while(text.isupper()):
    print("UPPER")
    break

"""
<<조건문-if, match case>>
if문 
    관계 연산
    >,<,>=,<=,==,!=
    논리 연산
    and, or
    
if 조건1:
    실행문
elif 조건2:
    실행문
elif 조건3:
    실행문
else:               //(조건1,2,3) 나머지
    실행문
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ    
match case (==switch case문)

match(변수):
    case ?:
        실행문             //break 안씀! 
    case ?:
        실행문 
    case _:                //==else
        실행문
"""

num=1

match(num):
    case 1:
        print("1이다")
    case 2:
        print("2다")
    case _:
        print("_")