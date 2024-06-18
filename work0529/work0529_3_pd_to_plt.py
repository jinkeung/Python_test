import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

lotus=load_iris()
data=lotus.data         #데이터
index=lotus.target      #해당 데이터의 분류 제목


iris_data=pd.DataFrame(data,index=index,columns=lotus.feature_names)

print(index)



for i in range(0,3):
    plt.scatter(data[index==i,0],data[index==i,1])
plt.show()



