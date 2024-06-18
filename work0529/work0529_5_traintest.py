import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split #분류[학습용, 테스트]
from sklearn.tree import DecisionTreeClassifier #머신러닝 모델
from sklearn.metrics import accuracy_score  #정확도 확인


iris=load_iris()
x=iris.data
y=iris.target

train_x, test_x, train_y, test_y\
= train_test_split(x,y, test_size=0.1, shuffle=True,random_state=3)
#학습할 테이터, 학습할 레이블

#print(train_x, test_x, train_y, test_y, sep="\n\n")


arr=np.array([1,2,3,4,5])
print(arr>=3)
