import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
'''
x=np.array(list(range(0,11)))
y=np.array(list(range(0,11)))
plt.xlabel('x label')
plt.ylabel('y label')
plt.plot(x,y)
plt.plot(x*2,y+1)
plt.title("TEST")
plt.legend(["Hello","World"])
plt.show()
'''

data=[[1,2,3,4,5],
      [4,2,3,4,5],
      [3,4,6,8,15],
      [5,4,9,1,10]]
label = [['A','B','C','D','E']]

pd_data=pd.DataFrame(data,columns=label)

for i in pd_data.columns:
    plt.plot(pd_data[i])

plt.show()

