from sklearn.metrics import accuracy_score,classification_report
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
import matplotlib.pyplot as plt

cali=fetch_california_housing()

data=cali.data
target=cali.target
features=cali.feature_names


df=pd.DataFrame(data=data,index=target,columns=features)


train_X, test_X, train_y, test_y=train_test_split(data,target, test_size=0.1, random_state=0)

model=LinearRegression()
model.fit(train_X,train_y)

y_pred=model.predict(test_X)

r2=r2_score(test_y,y_pred)     # 회귀 모델이 얼마나 잘 표현하는지
mean_squared_error=mean_squared_error(test_y,y_pred)

print(r2)
print(mean_squared_error)

print(df)
print(test_y)
print(y_pred)

plt.scatter(test_X[:,0],test_y)
plt.scatter(test_X[:,0],y_pred)
plt.legend(["Actual","Predicted"])
plt.show()