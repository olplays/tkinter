from tkinter import*

window=Tk()

def convert():
    grams=float(e2_value.get())*1000
    pounds=float(e2_value.get())*2.20462
    ounce=float(e2_value.get())*35.274
    
    t1.delete("1.0",END)
    t2.delete("1.0",END)
    t3.delete("1.0",END)
    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounce)
e1=Label(window,text="enter the value in kg")
e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e3=Label(window,text="grams")
e4=Label(window,text="pounds")
e5=Label(window,text="ounce")

t1=Text(window,height=1,width=20)
t2=Text(window,height=1,width=20)
t3=Text(window,height=1,width=20)

b1=Button(window,text="convert",command=convert)

e1.grid(row=0,column=0)
e2.grid(row=0,column=1)
e3.grid(row=1,column=0)
e4.grid(row=1,column=1)
e5.grid(row=1,column=2)

t1.grid(row=2,column=0)
t2.grid(row=2,column=1)
t3.grid(row=2,column=2)

b1.grid(row=0,column=2)

window.mainloop()