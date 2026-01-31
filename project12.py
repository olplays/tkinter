from tkinter import *
from time import strftime
root=Tk()
root.geometry("600x400")


def clock():
    day=strftime("%a")
    date=strftime("%d/%m/%Y")
    timee=strftime("%I:%M:%S %p")  
    
    
    time_zone=strftime("%Z")

    day_var.set(day)
    date_var.set(date)
    time_var.set(timee)
    zone_var.set(time_zone)
   

    time_entry.after(1000,clock)


day_var=StringVar()
date_var=StringVar()
time_var=StringVar()
zone_var=StringVar()
day_entry=Entry(root,textvariable=day_var,state="readonly",fg="red")
day_entry.grid(column=1,row=1)

date_entry=Entry(root,textvariable=date_var,state="readonly",fg="red")
date_entry.grid(column=2,row=1)

time_entry=Entry(root,textvariable=time_var,state="readonly",fg="red")
time_entry.grid(column=3,row=1)

zone_entry=Entry(root,textvariable=zone_var,state="readonly",fg="red")
zone_entry.grid(column=4,row=1)

Button(root,text="PRESS ME !!!", command=clock).grid(column=2,row=0)



root.mainloop()