import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=[[0,1,2,3,4],[10,4,2,8,10],[10,11,2,4,3],[5,2,1,5,6]]
df=pd.DataFrame(data,index=[0,1,2,3])


for i in range(0,len(df)):          # == df.shape[0]
    plt.plot(df.values[i])

plt.show()