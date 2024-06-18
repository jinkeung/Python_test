import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


'''
-figure[공간의 크기],axis[공간 분할[1,1]]
'''
'''
#fig: 레이어, axis: 축 (공간분할, 그래프들)
fig,ax=plt.subplots(nrows=2,ncols=2,figsize=(10,10))      #subplots 안썼을때 기본이 1 1
ax[0, 0].plot([1, 2, 3, 4, 5])
ax[0, 1].plot([5, 4, 3, 2, 1])

plt.show()
'''
'''
fig=plt.figure(figsize = (10,10))
fig.add_subplot(211)    # 2row x 1column 로 나눴을때 1번째
fig.add_subplot(337)    # 3row x 3column 로 나눴을때 7번째
fig.add_subplot(338)
fig.add_subplot(339)
plt.show()
'''

#matplotlib -> tkinter 데이터 전송 GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def click():
    fig, ax=plt.subplots(nrows=2, ncols=2,figsize=(5,5))
    ax[0, 0].plot(range(1,11))
    ax[0,1].pie(range(1,11))
    ax[1,0].bar(['a','b','c','d','e'], range(1,6))
    ax[1,1].hist((np.random.randn(100)*1000).round(0),bins=10)
    # => fig 에 전부 들어있음

    window=tk.Toplevel()
    window.geometry('800x800')
    frame=tk.Frame(window)
    canvas=FigureCanvasTkAgg(fig, frame)
    canvas.get_tk_widget().pack()
    frame.pack()



root=tk.Tk()
button=tk.Button(root,text="Click",command=click)
button.pack()
root.mainloop()