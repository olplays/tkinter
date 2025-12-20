import pyautogui
from tkinter import *
from tkinter import ttk
W,H=pyautogui.size()
print(pyautogui.size())
root=Tk()
root.geometry(f"{W}x{H}")
root.title("pizza delivery app")
root.config(background="red")
Label(root,text="pizza delivery",background="blue",foreground="red",borderwidth=5,relief="raised",font="roboto 20 bold",anchor="n",).grid(row=0,column=3)
Label(root,text="SELECT YOUR PIZZA",background="yellow", font="roboto 20").grid(row=1,column=2)
pizza_types=["cheese","pepperoni","vegetable","tandori"]
pizza_combo=ttk.Combobox(root,text="select your pizza",values=pizza_types)
pizza_combo.grid(row=2,column=2)
Radiobutton(root,text="LARGE",background="pink").grid(row=3,column=2)
Checkbutton(root,text="").grid(row=3,column=4)
root.mainloop()