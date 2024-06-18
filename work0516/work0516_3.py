'''
"먼저 자신을 비웃어라.
 다른 사람이 당신을 비웃기 전에."
	- 엘사 맥스웰.
'''

#end: 해당 구문이 완료 되었을 때, sep: 해당 구문이 구분 되었을 때만 출력
print('"먼저 자신을 비웃어라','\n 다른 사람이 당신을 비웃기 전에','"\n\t- 엘사 맥스웰',end=".",sep=".")
print()

arr1=list(range(2,10))
arr2=list(range(1,10))

# 2*1 ~ 2*9 // 3*1~3*9

for i in arr1:
    print(i,"단")
    for j in arr2:
        print("%d * %d = %d" %(i,j,i*j))
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")


arr1=list(range(1,6))
arr2=list(range(5,-1,-1))

for i,j in zip(arr1,arr2):               #in 뒤에는 하나의 객체만 올 수 있음
    print("i=%d, j=%d" %(i,j))           #  => zip읕 통해 하나의 객체 단위로 묶음


arr=[[1,2,3],[4,5,6],[7,8,9]]

for i in arr:               #i = arr[0],[1],[2]
    for j in i:
        print(j)




arr=list(range(1,6))
arr2=["Hello","World","Robot"]
arr3={}

for i,j in zip(arr,arr2):
    arr3[i]=j

print(arr3)


li={2:list(range(1,10))}

for i in li.keys():
    for j in li[i]:
        print("%d*%d=%d" %(i,j,i*j))





li2={}
for i in range(2,10):
    li2[i]=list(range(1,10))

for i in li2.keys():
    for j in li2[i]:
        print("%d*%d=%d" %(i,j,i*j))


for i in range(1,8,2):
    print("*"*i)

for i in range(1,6):
    print("*"*i)


#i=1, j=1 // i=2, j=1,2 // i=3, j=1,2,3

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print()


"""

_________*                  _:9 *: 1
________***                 _:8 *: 3
_______*****                _:7 *: 5
______*******               _:6 *: 7
_____*********              _:5 *: 9
____*_________*             4 1 9 1 
___***_______***            3 3 7 3
__*****_____*****           2 5 5 5
_*******___*******          1 7 3 7
*********_*********         0 9 1 9

"""

for i,j in zip(range(9,4,-1),range(1,10,2)):
    print(" "*i,"*"*j,sep="")
for i,j,k in zip(range(4,-1,-1),range(1,10,2),range(9,0,-2)):
    print(" "*i,"*"*j," "*k,"*"*j,sep="")

print()


for i,j in zip(range(1,6),range(5,0,-1)):
    print(" "*i," "*(j*2-1),"*"*(i*2-1))
for i,j in zip(range(1,6),range(5,0,-1)):
    print(" "*j,"*"*(i*2-1)," "*(j*2-1),"*"*(i*2-1))

print()
"""
*********       09              
_*******_       17
__*****__       25
___***___       33    
____*____       41 
"""

for i,j in zip(range(0,5),range(9,0,-2)):
    print(" "*i,"*"*j,sep="")
for i,j in zip(range(4,-1,-1),range(1,10,2)):
    print(" "*i, "*"*j,sep="")