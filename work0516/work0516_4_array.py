"""
<<배열-list,tuple,set>>
-list [리스트]: 배열[arr]과 동일시 [List, ArrayList 객체-자동적으로 공간이 할당]
-tuple (튜플): int arr[]=new int[5]-새로운 값을 추가, 삭제 불가
-set {집합}: 값의 순서가 없음
"""
#<<list>>
num=[1,2,3,4,5]
print(type(num))
print(num[1])

num=(1,2,3,4,5)
print(type(num))

num={1,2,3,4,5}
print(type(num))
# print(num[1]) => set은 위치값이 없음~

arr=[1,2,3,4,5]
print(arr)
arr2=list(range(1,6))
print(arr2)
arr3=tuple(range(1,10,2))
print(arr3)

#arr2=[1,2,3,4,5]
arr2[0]=10                            #정해진 위치 대입(수정)
print(arr2)

arr2.insert(0,20)       #정해진 위치에 추가
print(arr2)
arr2.append(30)                       #맨 뒤에 추가
print(arr2)
arr2.pop(0)                           #정해진 위치값의 데이터 삭제
print(arr2)
del(arr2[5])                          #정해진 위치값의 데이터 삭제
print(arr2)
arr2.remove(10)                       #정해진값과 일치하는 데이터 삭제
print(arr2)

arr=[1,56,4,2,9]
arr.sort()                             #정렬
print(arr)

arr.clear()                            #비우기
print(arr)

arr3=list(range(1,6))                   #[1,2,3,4,5]
#인덱싱[색인, 찾다]
print(arr3[0])
print(arr3[-1])                         #5
print(arr3[-2])                         #4

#슬라이싱
print(arr3[0:3])                        #0번째부터 2번째(3번째 전)까지
print(arr3[2:])                         #2번째부터 ~
print(arr3[:2])                         #(0번째부터) ~ 2번째(3번째 전) 까지

"""
-dictionary(딕셔너리[사전]) (==Map, Hash 객체)
                            ex) Map<String, String> test=HashMap<String, String>();
dictionary={"key":"value"}
"""
dic1={"apple":"red","banana":"yellow"}
print(dic1)
print(dic1.keys())
print(dic1["apple"])

dic2={"A":"Hello","B":"World"}
print(dic2)
print(dic2.items())
print(dic2.keys())
print(dic2.values())
dic2.update({"C":"Robot"})
dic2["D"]="HI"
print(dic2)
print(dic2["B"])

