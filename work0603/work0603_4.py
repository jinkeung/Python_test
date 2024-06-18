#iris의 데이터를 db에 적재
#target_num int, sepal_l number, sepal_w number, petal_l number, petal_w number


#1번째 창
    #tk이용, sepal_len~ petal_wid까지 [4가지] 값 입력
    #1번 버튼 클릭시, 해당 데이터 분류작업 수행, predic 값 출력하여 몇센트 정확한지 확인
    #해당 데이터를 데이터베이스에 적재하는 버튼
    #해당 창을 닫는 취소 버튼

from sklearn.datasets import load_iris
iris=load_iris()
data=iris.data
target=iris.target
features=iris.feature_names

import oracledb as db

'''
con=db.connect(dsn="192.168.0.35:1521/xe",user="c##python",password="1234")
cursor=con.cursor()
for i,j in zip(target,data):
    print(i,j[0],j[1],j[2],j[3])
    cursor.execute('insert into iris values(:a,:b,:c,:d,:e)',a=int(i),b=j[0],c=j[1],d=j[2],e=j[3])
con.commit()
cursor.close()
con.close()
'''

import tkinter as tk
import tkinter.messagebox as mbox
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def predict():

    def insert():
        con=db.connect(dsn="192.168.0.35:1521/xe",user="c##python",password="1234")
        cursor=con.cursor()

        try:
            cursor.execute('insert into iris values(:a,:b,:c,:d,:e)',a=int(predict[0]),b=float(e_1.get()),c=float(e_2.get()),d=float(e_3.get()),e=float(e_4.get()))
            con.commit()
            mbox.showinfo("insert","데이터 추가 성공")
        except Exception as e:
            mbox.showerror("error","데이터 추가 실패")
            print(e)
            pass
        cursor.close()
        con.close()

    def close():
        pre.destroy()
        e_1.delete(0,tk.END)
        e_2.delete(0,tk.END)
        e_3.delete(0,tk.END)
        e_4.delete(0,tk.END)

    con=db.connect(dsn="192.168.0.35:1521/xe",user="c##python",password="1234")
    cursor=con.cursor()


    try:
        cursor.execute('select * from iris')
        target=list()
        data=list()
        for i in cursor.fetchall():
            target.append(i[0])
            data.append(list(i[1:]))
        data=np.array(data)

        '''
        data=np.array(list(cursor.execute('select SEPAL_W, , , ,from iris))) 
        target=np.array(list(cursor.execute('select target_num from iris )))')
        한줄로 가져올수 있음. . . . .
        그냥 가져와서 저장 vs 전체가져와서 반복문150번 ?
        '''

        train_X, test_X, train_y, test_y = train_test_split(data, target, test_size=0.2, random_state=0)

        entry_li=[[e_1.get(),e_2.get(),e_3.get(),e_4.get()]]


        model=DecisionTreeClassifier()
        model.fit(train_X,train_y)                   #학습
        predict1=model.predict(test_X)
        accuracy=accuracy_score(test_y,predict1)


        accuracy=str(round(accuracy*100,2))+'%'
        predict=model.predict(entry_li)
        predict_name=""
        target_names=load_iris().target_names
        predict_name=target_names[int(predict[0])]

        pre=tk.Toplevel()
        pre.geometry('500x500')

        f_pre=tk.Frame(master=pre)
        l_6_1=tk.Label(f_pre,text='현재 정확도: ',font=('Helvetica',13))
        l_6_1.grid(row=0,column=0)
        l_6_2=tk.Label(f_pre,text=accuracy,font=('Helvetica',13))
        l_6_2.grid(row=0,column=1)
        l_1_1=tk.Label(f_pre,text='Predict: ',font=('Helvetica',13))
        l_1_1.grid(row=1,column=0)
        l_1_2=tk.Label(f_pre,text=predict_name,font=('Helvetica',13))
        l_1_2.grid(row=1,column=1)
        l_2_1=tk.Label(f_pre,text='Sepal Length',font=('Helvetica',13))
        l_2_1.grid(row=2,column=0)
        l_2_2=tk.Label(f_pre,text=e_1.get(),font=('Helvetica',13))
        l_2_2.grid(row=2,column=1)
        l_3_1=tk.Label(f_pre,text='Sepal Width',font=('Helvetica',13))
        l_3_1.grid(row=3,column=0)
        l_3_2=tk.Label(f_pre,text=e_2.get(),font=('Helvetica',13))
        l_3_2.grid(row=3,column=1)
        l_4_1=tk.Label(f_pre,text='Petal Length',font=('Helvetica',13))
        l_4_1.grid(row=4,column=0)
        l_4_2=tk.Label(f_pre,text=e_3.get(),font=('Helvetica',13))
        l_4_2.grid(row=4,column=1)
        l_5_1=tk.Label(f_pre,text='Petal Width',font=('Helvetica',13))
        l_5_1.grid(row=5,column=0)
        l_5_2=tk.Label(f_pre,text=e_4.get(),font=('Helvetica',13))
        l_5_2.grid(row=5,column=1)

        f_pre.pack(pady=10)

        b_insert=tk.Button(pre,text='Insert',font=('Helvetica',13),command=insert)
        b_insert.pack()
        b_close=tk.Button(pre,text='Close',font=('Helvetica',13),command=close)
        b_close.pack()

        pre.mainloop()
    except:
        mbox.showerror('ERROR','데이터를 입력해주세요')
        pass





home=tk.Tk()
home.geometry('500x500')
l_home=tk.Label(home,text='Iris Data',font=('Helvetica',13))
l_home.pack(pady=10)

f_home=tk.Frame(home)
l_1=tk.Label(f_home,text='Sepal Length',font=('Helvetica',13))
l_1.grid(row=0,column=0)
e_1=tk.Entry(f_home,font=('Helvetica',13))
e_1.grid(row=0,column=1)
l_2=tk.Label(f_home,text='Sepal Width',font=('Helvetica',13))
l_2.grid(row=1,column=0)
e_2=tk.Entry(f_home,font=('Helvetica',13))
e_2.grid(row=1,column=1)
l_3=tk.Label(f_home,text='Petal Length',font=('Helvetica',13))
l_3.grid(row=2,column=0)
e_3=tk.Entry(f_home,font=('Helvetica',13))
e_3.grid(row=2,column=1)
l_4=tk.Label(f_home,text='Petal Width',font=('Helvetica',13))
l_4.grid(row=3,column=0)
e_4=tk.Entry(f_home,font=('Helvetica',13))
e_4.grid(row=3,column=1)
f_home.pack()

b_predict=tk.Button(home,text='predict',font=('Helvetica',13),command=predict)
b_predict.pack(pady=10)


home.mainloop()

