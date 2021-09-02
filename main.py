from tkinter import *
from tkinter import ttk
import json
import pickle
import numpy as np

with open('banglore_home_prices_model.pickle', 'rb') as f1:
    model = pickle.load(f1)

f = open('columns.json','rb')
data = json.load(f)
list_location=[]
for i in data['data_columns']:
    list_location.append(i)
list1=list_location[:]
list_location.pop(0)
list_location.pop(0)
list_location.pop(0)

def get_estimated_price():
        location=get_location()
        loc_index = np.where(list1==location)
        x = np.zeros(len(list1))
        x[0] = get_area()
        x[1] = no
        x[2] = no_bhk
        global txt 
        txt = round(model.predict([x])[0],2)
        txt=str(txt)+" Lakhs"
        ans_final = Label(root,text=txt, bd =5,font=("times new roman",20,"bold"),width=14,bg='#F0D9FF',fg="#2A0944").place(x=220,y=510)
        txt=''
        ans_area.delete(0,'end')
        ans_loc.set('')
        estimate_btn.configure(state='disabled')
        ans_area.configure(state='disabled')
        btn1.configure(state='disabled')
        btn2.configure(state='disabled')
        btn3.configure(state='disabled')
        btn4.configure(state='disabled')
        btn5.configure(state='disabled')
        btn_1.configure(state='disabled')
        btn_2.configure(state='disabled')
        btn_3.configure(state='disabled')
        btn_4.configure(state='disabled')
        btn_5.configure(state='disabled')
        ans_loc.configure(state='disabled')
        
        estimate_again = Button(root,text="Estimate Again",padx=10,pady=5,command=clicked)
        estimate_again.configure(background='#2A0944', foreground='white',font=('calibri',17,'bold'))
        estimate_again.place(x=250,y=430)
        ans_area.delete(0,'end')
        
def clicked():
        btn1.config(state='normal')
        ans_area.configure(state="normal")
        btn1.configure(state='normal')
        btn2.configure(state='normal')
        btn3.configure(state='normal')
        btn4.configure(state='normal')
        btn5.configure(state='normal')
        btn_1.configure(state='normal')
        btn_2.configure(state='normal')
        btn_3.configure(state='normal')
        btn_4.configure(state='normal')
        btn_5.configure(state='normal')
        ans_loc.configure(state='normal')
        get_estimated_price()

def which_bhk(bhk):
    global no_bhk
    no_bhk=bhk
    # return bhk

def which_bath(bath):
    global no
    no=bath
    # return bath

def get_area():
    ar= ans_area.get()
    return ar

def get_location():
    return ans_loc.get()

root=Tk()
root.geometry('700x600+300+50')
root.title('Home Price rediction | BY SHAILZA')
root.configure(background='#F0D9FF')
root.iconbitmap("icon.ico")
root.resizable(width=False,height=False)

label_main=Label(root,text="Home Price Prediction",font=("times new roman",30,"bold"),bd=10,relief=GROOVE,bg='#2A0944',fg="white").pack(side=TOP,fill=X)

label_area=Label(root,text="Area(Square feet)",font=("times new roman",20,"bold"),bg='#F0D9FF',fg="#2A0944")
label_area.place(x=100,y=140)

def only_numbers(char):
    return char.isdigit()

validation = root.register(only_numbers)
ans_area = Entry(root,validate="key", validatecommand=(validation, '%S') ,bd =5,font=("times new roman",20,"bold"),width=14,bg='white',fg="#2A0944")
ans_area.place(x=350,y=140)

label_bhk=Label(root,text="BHK",font=("times new roman",20,"bold"),bg='#F0D9FF',fg="#2A0944").place(x=100,y=200)

btn1 = Button(root,text="1",padx=10,pady=5,command=lambda m=1: which_bhk(m))
btn1.configure(background='white', foreground='#2A0944',font=('calibri',12,'bold'))
btn1.place(x=350,y=200)
btn2 = Button(root,text="2",padx=10,pady=5,command=lambda m=2: which_bhk(m))
btn2.configure(background='white', foreground='#2A0944',font=('calibri',12,'bold'))
btn2.place(x=390,y=200)
btn3 = Button(root,text="3",padx=10,pady=5,command=lambda m=3: which_bhk(m))
btn3.configure(background='white', foreground='#2A0944',font=('calibri',12,'bold'))
btn3.place(x=430,y=200)
btn4 = Button(root,text="4",padx=10,pady=5,command=lambda m=4: which_bhk(m))
btn4.configure(background='white', foreground='#2A0944',font=('calibri',12,'bold'))
btn4.place(x=470,y=200)
btn5 = Button(root,text="5",padx=10,pady=5,command=lambda m=5: which_bhk(m))
btn5.configure(background='white', foreground='#2A0944',font=('calibri',12,'bold'))
btn5.place(x=510,y=200)

label_bath=Label(root,text="No of Bathrooms",font=("times new roman",20,"bold"),bg='#F0D9FF',fg="#2A0944").place(x=100,y=260)

btn_1 = Button(root,text="1",padx=10,pady=5,command=lambda m=1: which_bath(m))
btn_1.configure(background='white', foreground='#2A0944',font=('calibri',12,'bold'))
btn_1.place(x=350,y=260)
btn_2 = Button(root,text="2",padx=10,pady=5,command=lambda m=2: which_bath(m))
btn_2.configure(background='white', foreground='#2A0944',font=('calibri',12,'bold'))
btn_2.place(x=390,y=260)
btn_3 = Button(root,text="3",padx=10,pady=5,command=lambda m=3: which_bath(m))
btn_3.configure(background='white', foreground='#2A0944',font=('calibri',12,'bold'))
btn_3.place(x=430,y=260)
btn_4 = Button(root,text="4",padx=10,pady=5,command=lambda m=4: which_bath(m))
btn_4.configure(background='white', foreground='#2A0944',font=('calibri',12,'bold'))
btn_4.place(x=470,y=260)
btn_5 = Button(root,text="5",padx=10,pady=5,command=lambda m=5: which_bath(m))
btn_5.configure(background='white', foreground='#2A0944',font=('calibri',12,'bold'))
btn_5.place(x=510,y=260)

label_location=Label(root,text="Location ",font=("times new roman",20,"bold"),bg='#F0D9FF',fg="#2A0944").place(x=100,y=320)

n = StringVar()
ans_loc = ttk.Combobox(root, width = 23, textvariable = n)
ans_loc.configure(background='#2A0944', foreground='white',font=('calibri',12,'bold'))
ans_loc['values'] =tuple(list_location[:] )
ans_loc.current(0) 
ans_loc.place(x=350,y=330)

estimate_btn = Button(root,text="Estimate Price",padx=10,pady=5,command=get_estimated_price)
estimate_btn.configure(background='#2A0944', foreground='white',font=('calibri',17,'bold'))
estimate_btn.place(x=250,y=430)

root.mainloop()
