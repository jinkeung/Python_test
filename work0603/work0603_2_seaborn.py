import matplotlib.pyplot as plt
#그래프 표현
    #세부적인 레이블, axis 조정
    #고차원적인 인터페이스 표현 불가능
'''    
plt.plot([1,2,3,4,5])
plt.xlabel('value X')
plt.ylabel('value Y')
plt.legend(["data"])
plt.axis([1,10,1,5])        #xlim(1~10) + ylim(1~5)
plt.show()
'''

import seaborn as sea
#그래프 표현
    #matplotlib가 표현이 불가능한 인터페이스의 표현 가능
    #matplotlib와 같은 세부적인 사항은 조정이 불가능


import pandas as pd
'''
#꽃종류 별로 각 특성 평균(바)
data=sea.load_dataset("iris")       #깃허브에 여러가지 dataset들 저장돼있음
pd_data=data.groupby("species")

figure=plt.figure(figsize=(10,10))
'''

'''
for i, data_Set in enumerate(pd_data):
    figure.add_subplot(311+i)
    sea.barplot(data_Set[1])
    plt.title(data_Set[0])

'''
'''
for i, j in zip(range(0,3),pd_data):
    figure.add_subplot(311+i)
    sea.barplot(j[1])
    plt.title(j[0])
plt.show()
'''

'''
#꽃 종류별로 sepal_length의 평균
data=sea.load_dataset("iris")
mean_data=data.groupby("species")["sepal_length"].mean().reset_index()
print(mean_data)

sea.barplot(data=mean_data,x=mean_data["species"],y=mean_data["sepal_length"])
plt.show()
'''
import pandas as pd
#꽃 setoas, virginica 만 sepla_length, sepal_width 평균 ax2개
data=sea.load_dataset("iris")
mean_data=data.groupby("species").mean().reset_index()

sample = mean_data.loc[[0,2],["sepal_length","sepal_width"]]
print(sample)


figure=plt.figure(figsize=(10,10))
for i in range(len(sample)):
    ax=figure.add_subplot(211+i)
    print(sample.iloc[i])
    sea.barplot(data=sample.iloc[i])


plt.show()


