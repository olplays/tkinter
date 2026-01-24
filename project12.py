from tkinter import *
from time import strftime
root=Tk()
time_text=Label(root,text="time will be displayed here :)")


def clock():
    timee=strftime("%I:%M:%S %p  %a %d/%m/%Y %Z")
    time_text.config(text=timee) 
    time_text.after(1000,clock)

Button(root,text="PRESS ME !!!", command=clock).pack()
time_text.pack()


root.mainloop()