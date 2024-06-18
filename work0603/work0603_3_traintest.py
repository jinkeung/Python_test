from sklearn.datasets import load_iris  #데이터셋
from sklearn.model_selection import train_test_split
#값에 대한 분류 [ train: 지도 데이터, test: 테스트용 데이터]
from sklearn.tree import DecisionTreeClassifier
#지도학습
from sklearn.metrics import accuracy_score, classification_report
#학습 평가
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
#scikit-learn: 머신러닝, 기계학습 오픈소스 외부라이브러리
              [지도, 비지도학습]
    1. 값에 대한 분류[train_test_split]
        -train: 지도 데이터
        -test: 테스트용 데이터
    2. 지도학습[ex) 알고리즘 적용, DecisionTreeClassifier]
    3. 학습 평가 [accuracy_score, classification_report]
        
    #지도학습
        #회귀[Regression]: 연속성인 변수의 값을 도출 (ex 선형 회귀)
        #분류[Classifier]: 특정한 값에 대한 분류 작업 (단, logistic regression=> 분류)
    #비지도학습
        #군집화[k-means clustering]: 비슷한 특성을 가진 데이터끼리의 묶음[그룹화]
        #차원축소: 데이터 시각화 등을 위하여 값의 최소화      
'''

import seaborn as sea

iris=load_iris()
data=iris.data
print(data)
print(type(data))

index=iris.target
feature_name=iris.feature_names
for i, lable in enumerate(iris.target_names):
    plt.scatter(x=data[index == i, 0], y=data[index == i, 1])
plt.show()



train_X, test_X, train_y, test_y= train_test_split(data,index,train_size=0.9,shuffle=True)
#train_size와 test_size중 하나만 작성(default:합계1)
#random_state() : 랜덤이지만 ()안의 값에따라 각기 다른 랜덤저장됨 (==c: srand()) => 난수 고정
#shupple: (default: true)
print(test_y)

model=DecisionTreeClassifier()
model.fit(train_X,train_y)      #지도학습

y_pred=model.predict(test_X)
print(y_pred)

accuracy=accuracy_score(test_y,y_pred)
print(accuracy)


print(classification_report(test_y,y_pred))

