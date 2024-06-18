import requests
from bs4 import BeautifulSoup as bs
import tkinter as tk
from tkinter import ttk
import webbrowser


response=requests.get('https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EB%84%B7%EB%A7%88%EB%B8%94')

if response.status_code == 200:
    web=bs(response.text,'lxml')
    titles = web.find_all('a', attrs={'class': ['news_tit', 'elss sub_tit']})

    data=list()
    for i in titles:
        data.append([i.get_text(),i["href"]])
    print(data)

home=tk.Tk()
home.geometry('1000x500')

f_home=tk.Frame(home)
l_box=tk.Listbox(f_home,width=60,height=10)
for i,j in zip(data,range(0,20)):
    l_box.insert(tk.END,i[0])

scroll=ttk.Scrollbar(f_home,orient=tk.VERTICAL)
scroll.pack(side=tk.RIGHT,fill=tk.Y)
l_box.config(yscrollcommand=scroll.set)

l_box.pack()

f_home.pack()
home.mainloop()