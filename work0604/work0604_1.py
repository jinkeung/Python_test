from pynput.keyboard import Key, Listener
#STDINPUT [기본적인 입력 장치]

import tkinter as tk
from tkinter import ttk
#표준 GUI 내장라이브러리

import numpy as np
import pandas as pd
import scipy as sci
#1차원 2차원 배열 구현, 과학적 수학 계산

import matplotlib.pyplot as plt
import seaborn as sns
#그래프 구현 라이브러리

import requests
import bs4 as bs        #beautifulsoup4
#웹 페이지 크롤링

from sklearn.tree import DecisionTreeClassifier  #pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.datasets import load_iris
#머신 러닝
'''
    머신러닝[기계 학습]
        : 기계에 특정한 데이터들을 쌓아서 어떠한 도출 값을 확인
         - 알고리즘
         - 자료구조
         - scipy[통계, 수학 계산]    
'''
#지도 학습: 데이터, 결과값
iris=load_iris()
X=iris.data
y=iris.target


'''
for i, lable in enumerate(iris.target_names):
    plt.scatter(X[y==i,0],X[y==i,1])
plt.show()
'''
# 학습용(train), 테스트용(test)
train_X, test_X, train_y, test_y=train_test_split(X,y, test_size=0.2)


mo=DecisionTreeClassifier()
mo.fit(train_X,train_y) # 학습용 데이터 제공 ( X에 해당하는 ->y)
predict=mo.predict(test_X) # 예측위해 새로운 데이터 제공
                           # 아까만든 test용 제공해도되고, 다른 리스트 제공해도됨
print(test_y)
print(predict)

auuracy=accuracy_score(test_y,predict)
print(auuracy)
