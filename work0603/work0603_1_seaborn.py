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
'''
#선형
plt.plot()      :
sea.lineplot()  :
#막대 그래프
plt.bar() 
sea.barplot()
#히스토그램
plt.hist()  
sea.histplot()
#산점도
plt.scatter()
sea.sactterplit()
#etc..
sea.boxplot()
sea.violinplot()
'''

data=sea.load_dataset("iris")       #깃허브에 여러가지 dataset들 저장돼있음
print(data)

sea.lineplot(data=data)
plt.show()

sea.barplot(data=data)
plt.show()

sea.boxplot(data=data)
plt.show()

sea.violinplot(data=data)
plt.show()

sea.histplot(data=data)
plt.show()

sea.scatterplot(data=data)
plt.show()