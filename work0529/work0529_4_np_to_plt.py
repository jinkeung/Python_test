import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data= [ [189.,  37.,  52.],
        [193.,  38.,  58.],
        [162.,  35.,  62.],
        [189.,  35.,  46.],
        [182.,  36.,  56.],
        [211.,  38.,  56.],
        [167.,  34.,  60.],
        [176.,  31.,  74.],
        [154.,  33.,  56.],
        [169.,  34.,  50.]]

target=['A','B','A','C','A','B','C','A','C','B']

pd=pd.DataFrame(data,index=target)
x=np.array(pd)                          # == pd.to_numpy()
y=np.array(pd.index)
print(x)
print(y)

for i in ['A','B','C']:
        plt.scatter(x[y==i,1],x[y==i,2])
plt.show()



