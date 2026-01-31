
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
W=600
H=400
root=Tk()
root.geometry(f"{W}x{H}")
root.title("stopwatch")
root.config(background="red")

Label(root,text="stopwatch", font="roboto 30").pack()
def start_counter():
    pass
hour_var=StringVar(value="00")
min_var=StringVar(value="00")
sec_var=StringVar(value="00")
Entry(root,textvariable=hour_var).place(x=100,y=100)
Entry(root,textvariable=min_var).place(x=200,y=100)
Entry(root,textvariable=sec_var).place(x=300,y=100)
Button(root,text="START",command=start_counter).place(x=200,y=300)



root.mainloop()