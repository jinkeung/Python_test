#정적크롤링[모든데이터 긁어오기]

import requests
#Server 정보 요청[Get]-HTML
from bs4 import BeautifulSoup as bs
#HTML, XML 파싱
import tkinter as tk
from tkinter import ttk
import webbrowser

def openLink():


    try:
        link=tv.item(tv.selection())["values"][0]
        webbrowser.open(link)
        con_response=requests.get(link)
        content=bs(con_response.text,"lxml")
        sub=tk.Tk()
        sub.geometry("1500x500")
        label=tk.Label(sub)
        label.pack()
        if link.startswith("https://www.mk"):
            for i in content.find_all("div",class_="view_txt"):
                label.config(text=i.text.replace(".","\n").strip())
        sub.mainloop()
    except requests.exceptions.ConnectionError:
        tv.delete(tv.selection())

def search():
    key=entry.get()
    response=requests.get("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%s" %key)
    if response.status_code == 200:
        web = bs(response.text, "lxml")


        for i in tv.get_children():
            tv.delete(i)

        title=web.find_all("a",{"class":"news_tit"})
        for i in title:
            tv.insert("","end",text=i.text,values=(i["href"]))
        tv.grid(row=0,column=0)


        for i in title:
            try:
                link=i["href"]
                response=requests.get(link)
                content=bs(response.text,"lxml")
                try:
                    for i in range(1,7):
                        hs=content.find_all("h"+str(i))
                        for i in hs:
                            print(i.text)
                except Exception:
                    pass
            except Exception:
                pass


response=requests.get("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EB%84%B7%EB%A7%88%EB%B8%94")
#print(response)        #200
if response.status_code==200:
    web=bs(response.text,"lxml")    #C언어로 구현

    root=tk.Tk()
    root.geometry('800x500')
    tv=ttk.Treeview(root,columns=["link","sub"],displaycolumns=["sub"])
    tv.column("#0", width=300)
    tv.column("link",width=300)
    tv.column("sub",width=500)
    tv.heading("#0",text="title")
    tv.heading("link",text="link")
    tv.heading("sub",text="sub")
    title=web.find_all("a",{"class":"news_tit"})


    for i in title:
        try:
            link=i["href"]
            response=requests.get(link)
            content=bs(response.text,"lxml")
            try:
                for j in range(1,7):
                    hs=content.find_all("h"+str(j))
                tv.insert("","end",text=i.text,values=(i["href"],"?"))
            except Exception:
                pass
        except Exception:
            pass


    tv.grid(row=0,column=0,pady=10)
    button=tk.Button(text="링크 이동",command=openLink)
    button.grid(row=1,column=0,pady=10)

    entry=tk.Entry(root)
    entry.grid(row=2,column=0,pady=10)
    button2=tk.Button(text="검색", command=search)
    button2.grid(row=3,column=0,pady=10)




    root.mainloop()