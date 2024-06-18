"""
    pandas: 외부 라이브러리
    -데이터[1,2,3차원 배열 필드]
    -dictionary 형태로 생성
    -1차원 배열 출력 : Series(data,index,dtype)
                        └data="1차원 배열 데이터 [값]", index="레코드 구분하기 위한 제목"
                    -행(index) 기반
    -2차원 배열 출력: DataFrame(data, index, columns[필드])
                        └data="2차원 배열 데이터 [값]", index="레코드 구분하기 위한 제목",
                         columns="2차원 배열 필드명"
                    -열(column) 기반
"""
import pandas as pd
import numpy as np



arr=np.arange(1,5)                                      #[1 2 3 4]
pd_Se=pd.Series(data=arr,index=['A','B','C','D'])

print(pd_Se['A'])                                       # => dictionary 형태임, 행(index)기반
print(pd_Se)

arr=np.arange(1,13).reshape(3,4)
pd_Da=pd.DataFrame(data=arr,index=['I1','I2','I3'],columns=['C1','C2','C3','C4'])
print(pd_Da)
print(pd_Da['C1'])

arr={'Hello':['A','B','C','D'],
     'World':['E','F','G','H'],
     'Robot':['I','J','K','L']}
pd_Da=pd.DataFrame(data=arr,index=['I1','I2','I3','I4'])
print(pd_Da)
print(pd_Da['Robot'])

pd_Da['Hello']=['D','C','B','A']
print(pd_Da)
print()
print(pd_Da.keys())
print(pd_Da.values)
print(pd_Da.ndim)

pd_Da['Hello']=['A','B','B','C']
print(pd_Da.describe())

del pd_Da['Robot']
print(pd_Da)

pd_Read=pd.read_excel("test.xlsx")
print(pd_Read)
pd_Read.to_excel("hello.xlsx")
pd_Read.to_csv("hello.csv")
