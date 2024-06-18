import requests
from bs4 import BeautifulSoup as bs
import tkinter as tk
from tkinter import ttk
import webbrowser
import tkinter.messagebox as mbox
import pandas as pd

def click():
    try:
        link=tv.item(tv.selection(),"values")
        link=link[0]
        webbrowser.open(link)
    except:
        mbox.showinfo('INFO',"선택하세요")
        pass



ne="넷마블"
response=requests.get('https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%s' % ne)

if response.status_code == 200:
    web=bs(response.text,'lxml')
    titles = web.find_all('a', attrs={'class': ['news_tit','elss sub_tit']})

    data=list()

    for i in titles:
        if(i['href'].startswith('https://www.mk')
            or i['href'].startswith('https://game.donga.')
            or i['href'].startswith('https://weekly.cnbnews.')
            or i['href'].startswith('https://news.mtn')
            or i['href'].startswith('https://www.econovill')
            or i['href'].startswith('https://www.asiatime.')):
            data.append([i.get_text(),i["href"]])

    data=data[0:10]
    content_li=list()

    for i in data:
        content_response=requests.get(str(i[1]))
        if content_response.status_code == 200:
            content_web=bs(content_response.text,'lxml')

        if (i[1].startswith('https://www.mk.')):
            content=content_web.find("div",class_="view_txt")
            content_li.append((content.get_text()).strip())
        elif(i[1].startswith('https://game.donga.')):
            content=content_web.find("div",class_="article")
            content_li.append((content.get_text()).replace("\n", ""))
        elif(i[1].startswith('https://weekly.cnbnews.')):
            content=content_web.find("div",class_="smartOutput")
            content_li.append((content.get_text()).replace("\n", ""))
        elif(i[1].startswith('https://news.mtn')):
            content=content_web.find("div",class_="css-16jbccu")
            content_li.append((content.get_text().strip()))
        elif(i[1].startswith('https://www.econovill')):
            content=content_web.find("div",class_="article-body")
            content_li.append((content.get_text().replace("\n", "")))
        elif(i[1].startswith('https://www.asiatime.')):
            content=content_web.find("div",class_="row article_txt_container")
            content_li.append((content.get_text().replace("\n", "")))




    home=tk.Tk()
    home.geometry('1000x500')

    f_home=tk.Frame(home)
    tv=ttk.Treeview(master=f_home,columns=['link','contents'],displaycolumns=['contents'])
    tv.column('#0',width=300)
    tv.column('link', width=200)
    tv.column('contents',width=1000)
    tv.heading('#0',text='title')
    tv.heading('link',text='link')
    tv.heading('contents',text='contents')


    for i,j in zip(data,content_li):
        tv.insert(parent="",text=i[0],values=[i[1],j],index=tk.END)


    scroll=tk.Scrollbar(f_home,orient=tk.VERTICAL,command=tv.yview)
    scroll.pack(side=tk.RIGHT,fill=tk.Y)
    tv.config(yscrollcommand=scroll.set)

    scroll2=tk.Scrollbar(f_home,orient=tk.HORIZONTAL,command=tv.xview)
    scroll2.pack(side=tk.BOTTOM,fill=tk.X)
    tv.config(xscrollcommand=scroll2.set)

    style = ttk.Style()
    style.configure("Treeview", rowheight=50)



    tv.pack(fill=tk.BOTH, expand=True)
    f_home.pack()

    b_link=tk.Button(text="링크 이동", command=click)
    b_link.pack(pady=10)
    home.mainloop()







