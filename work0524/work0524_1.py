#tkinter [표준 GUI 구현 라이브러리], matplotlib[GUI 그래프 구현 라이브러리]
import tkinter as tk

window=tk.Tk()     #form, window창 구현
window.title("0524 window")
window.geometry("1000x500+900+100")
window.resizable(True,False)

'''
#Label, Button, Entry, ListBox, Treebox, Frame

label1=tk.Label(master=window,text="라벨11111",bg="pink",fg="white",font=("",20))
label2=tk.Label(master=window,text="라벨2",bg="purple",fg="white",font=("",20))
label3=tk.Label(master=window,text="라벨3",bg="violet",fg="white",font=("",20)
                ,width=15)

label4=tk.Label(master=window,text="라벨4",bg="blue",fg="white",font=("",20))

label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0,columnspan=2)

label4.place(x=50,y=0)

entry1=tk.Entry(window,width=30, font=("",20))
entry1.grid(row=3,column=0)

def click():
    if entry1.get():
        label2.configure(text=entry1.get())

button1=tk.Button(text="버튼1",font=("",20),command=click)
button1.grid(row=3,column=1)
'''

#iframe [window 하위 새로운 레이어 생성]
Frame1=tk.Frame(master=window,relief="solid")
label1=tk.Label(master=Frame1,text="라벨11111",bg="pink",fg="white",font=("",20))
label1.pack()
button1=tk.Button(master=Frame1,text="버튼1",font=("",20))
button1.pack()
Frame1.pack(side=tk.LEFT)


Frame2=tk.Frame(master=window, relief="solid")
label2=tk.Label(master=Frame2,text="라벨2",bg="violet",fg="white",font=("",20))
label2.pack()
button2=tk.Button(master=Frame2,text="버튼2",font=("",20))
button2.pack()
Frame2.pack(side=tk.RIGHT)



window.mainloop()