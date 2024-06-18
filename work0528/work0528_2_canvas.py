import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry('700x700')
canvas=tk.Canvas(root,bg="white",height=500,width=500)
canvas.pack()
canvas.create_line(0,200,500,100,fill="black")
#canvas.create_image()
root.mainloop()
