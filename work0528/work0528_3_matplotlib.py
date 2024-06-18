'''
-matplotlib[Matrix plot library]
: GUI를 통해 그래프 생성

-그래프[차트]
    : 표[테이블]를 도형화 시킨 개체
        ex)막대, 선형, 산점도, 히스토그램 . . .

    -차트 영역(차트 전체 영역)
        1) 가로축[x label], 세로축[y label]: 데이터의 상세한 정보
        2) 범례[legend]: 계열의 표기 등
        3) 차트 제목[title]
        4) 데이터 표(테이블)
    -그림 영역
        1) 데이터 계열(data): 막대[bar], 선, 점 . . .
        2) 데이터 레이블 : 데이터 계열의 값?
        3) 눈금선 . . .

-figure[공간의 크기],axis[공간 분할[1,1]]
'''

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.figure as figure
#선형 그래프-데이터 축 2개(x,y) 필수

x=np.array(list(range(1,6)))
y=np.array(list(range(1,6)))
plt.plot(x,y)                  #기본 x,y축 필요
plt.plot([10,5,4,7,2])              #데이터 추가
plt.plot(list(range(10,5,-1)))      #데이터 추가
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("TITLE")
plt.legend(["l1","l2","l3"],loc="upper center")
plt.show()

#막대 그래프 - x[레이블], y[숫자데이트]
plt.bar(['a','b','c'],[1,2,3])
plt.show()

#산점도
plt.scatter(['1','2','3','4','5'],[1,2,3,4,5])
plt.show()

#히스토그램: 분포[평균]를 구할 때 사용하는 막대 그래프
arr= (np.random.randn(100)*1000).round(-1)
print(arr)
plt.hist(arr,bins=20)
plt.show()

#원형 그래프[파이차트] - 데이터 축 1개
plt.pie([10,20,30,40],labels=['a','b','c','d'])
plt.show()

