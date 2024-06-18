"""
    라이브러리?
    -내부 라이브러리: 설치 되어져 있는 함수들 모음
    -외부 라이브러리: (내부 라이브러리 이외) 호출필요
        -설치: pip[Python install Package] install 라이브러리(ex.numpy)
            (-pip도 업데이트 필요함 : python -m pip install --upgrade pip)
        -업데이트: pip install --upgrade 라이브러리
        -삭제: pip uninstall 라이브러리
        -불러오기: import 라이브러리
"""

"""
    numpy: 외부 라이브러리
    - 계산 작업을 위한 라이브러리
    - 1,2차원 배열[list,tuple 등]의 형태를 취한다
    
"""

import numpy as np
                                    #numpy배열 만들기
arr=np.array(list(range(1,5)))      #[1 2 3 4]
arr2=np.zeros(5)                    #[0. 0. 0. 0. 0.]
arr3=np.ones(5)                     #[1. 1. 1. 1. 1.]
arr4=np.full(5,3)      #[3 3 3 3 3]
arr5=np.arange(1,5)                 #[1 2 3 4]


print(type(arr))                    #numpy.ndarray
print(arr.dtype)                    #int32
print(arr.ndim)                     #1 (차원)
print(arr.sum())                    #1+2+3+4 => 10
print(arr+arr5)                     #[1 2 3 4]+[1 2 3 4] => [2 4 6 8]
print(np.multiply(arr,arr))         #[1 2 3 4]*[1 2 3 4]=>[1 4 9 16]
print(np.subtract(arr,arr))         #[0 0 0 0]

li= [1,2,3,4]
li2=[1,2,3,4]                       #cf) 리스트
print(li+li2)                       #[1,2,3,4,1,2,3,4]

arr6=np.arange(1,13).reshape(3,4)   #[1~9] => 3x3(2차원 배열)형태로 변경
print(arr6)

