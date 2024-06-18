'''
N,M=map(int,input().split())
arr=list(range(1,N+1))

temp=0

for i in range(0,M):
    a,b=map(int, input().split())
    temp=arr[a-1]
    arr[a-1]=arr[b-1]
    arr[b-1]=temp

for i in arr:
    print(i,end=" ")
'''
'''
arr=list(range(1,31))
print(arr)
for i in range(1,29):
    arr.remove(int(input()))
for i in arr:
    print(i)
'''


import sys
N=int(sys.stdin.readline())
stack=[]

for i in range(0,N):
    command,X=map(str,sys.stdin.read().split())
    X=int(X)
    print(command,X)

