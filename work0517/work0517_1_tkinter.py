import tkinter as tk
#파이썬 표준 GUI 툴

window=tk.Tk()

window.geometry('500x500+0+0')
window.title('Hello World')

button=tk.Button(window,text='Click', width=10, height=10)
button.pack()

window.mainloop()
