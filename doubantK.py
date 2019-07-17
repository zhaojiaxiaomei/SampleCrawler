from tkinter import *
from tkinter import ttk
win = Tk()
win.title('tk')
win.geometry('1000x700')
import tkinter as tk
from doubanData import run,Selectcountry,randomMovie
from PIL import Image, ImageTk
import pandas as pd
f = open('movieTop250.csv', encoding='UTF-8')
df = pd.read_csv(f)
var1=tk.StringVar()
def b1():
    imglabel.grid(row=2, columnspan=2)
    b3.grid(row=1, column=1)
    b2.grid(row=1, column=0)
b1 = Button(win, text='爬取豆瓣Top250电影', command=b1)
b1.grid(columnspan=2)


def b2():
    top2 = Toplevel()
    top2.title('韩田慧按照国家筛选')
    cmb = ttk.Combobox(top2, width=12)
    cmb.place(x=10, y=10)
    cmb['value'] = ('中国大陆', '美国', '日本','香港','英国','其他')
    cmb.current(0)
    cmb.grid(row=0, sticky=W, padx=4)
    def b():
        c = cmb.get()
        rl=Selectcountry(c,df)
        var2.set(rl)
    b = Button(top2, text='查询', command=b)
    b.grid(row=0, column=1, sticky=W)
    l0 = Label(top2, text='电影名及简介')
    l0.grid(row=1, sticky=W)
    var2 = tk.StringVar()
    lb = Listbox(top2, listvariable=var2, width=100,height=200)
    lb.grid(row=2, columnspan=3)


b2 = Button(win, text='国家筛选', command=b2)


def b3():
    top3 = Toplevel()
    top3.title('韩田慧随便看看')
    var0 = tk.StringVar()
    var1 = tk.StringVar()
    var2 = tk.StringVar()
    def b4():
        global s
        movie=randomMovie(df)
        var0.set(movie[0]['name'])
        var1.set(movie[0]['director_actor'])
        var2.set(movie[0]['introduce'])
    b4 = Button(top3, text='随便看看', command=b4)
    b4.grid(row=0, columnspan=2)
    lname0 = Label(top3,text='电影名：')
    lname0.grid(row=1)
    lname01 = Label(top3,textvariable=var0,bg='white',width=100)
    lname01.grid(row=1, column=1)
    lname1 = Label(top3,text='导演和主演：')
    lname1.grid(row=2)
    lname11 = Label(top3,textvariable=var1,bg='white',width=100)
    lname11.grid(row=2, column=1)
    lname2 = Label(top3,text='简介：')
    lname2.grid(row=3)
    lname21 = Label(top3,textvariable=var2,bg='white',width=100)
    lname21.grid(row=3, column=1)


b3 = Button(win, text='随便看看', command=b3)
img = Image.open('year.png')  # 打开图片
photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
imglabel = Label(win, image=photo)
win.mainloop()