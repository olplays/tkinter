import pyautogui
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
W,H=pyautogui.size()
print(pyautogui.size())
root=Tk()
root.geometry(f"{W}x{H}")
root.title("pizza delivery app")
root.config(background="red")
Label(root,text="pizza delivery",background="blue",foreground="red",borderwidth=5,relief="raised",font="roboto 20 bold",anchor="n",).grid(row=0,column=3, pady=20)
Label(root,text="SELECT YOUR PIZZA",background="yellow", font="roboto 20").grid(row=1,column=2,padx=20,pady=20)

pizza_types=["cheese","pepperoni","vegetable","tandori"]
pizza_var=StringVar()
pizza_combo=ttk.Combobox(root,textvariable=pizza_var,values=pizza_types,font="roboto 20")
pizza_combo.grid(row=1,column=3,padx=20,pady=20)
pizza_combo.current(0)
size_label=Label(root,text="SELECT YOUR SIZE",background="yellow", font="roboto 20").grid(row=2,column=1,padx=20,pady=20)

size=StringVar(value="small")
Radiobutton(root,text="LARGE",background="pink", font="roboto 15",variable=size,value="large").grid(row=3,column=1,padx=20,pady=20)
Radiobutton(root,text="MEDIUM",bg="red", font="roboto 15",variable=size,value="medium").grid(row=4,column=1,padx=20,pady=20)
Radiobutton(root,text="SMALL",bg="yellow", font="roboto 15",variable=size,value="small").grid(row=5,column=1,padx=20,pady=20)

Label(root,text="SELECT YOUR TOPPINGS",background="yellow", font="roboto 20").grid(row=2,column=4,padx=20,pady=20)

pepperoni=BooleanVar()
mushrooms=BooleanVar()
onions=BooleanVar()


Checkbutton(root,text="pepperoni", font="roboto 15",variable=pepperoni).grid(row=3,column=4,padx=20,pady=20)
Checkbutton(root,text="mushrooms", font="roboto 15",variable=mushrooms).grid(row=4,column=4,padx=20,pady=20)
Checkbutton(root,text="onions", font="roboto 15",variable=onions).grid(row=5,column=4,padx=20,pady=20)


spin=Spinbox(root, font="roboto 15",from_=1,to=10)
spin.grid(row=7,column=3,pady=20)

Label(root,text="QUANTITY OF PIZZAS",font="roboto 20").grid(row=6,column=3,pady=20)

Label(root,text="SELECT DRINKS",background="yellow", font="roboto 20").grid(row=1,column=5,padx=20,pady=20)
drinks=["Coke","Pepsi","Fanta","Sprite"]
drink_var=StringVar()
drink_combo=ttk.Combobox(root,textvariable=drink_var,values=drinks,font="roboto 20")
drink_combo.grid(row=1,column=6,padx=20,pady=20)
drink_combo.current(0)



def order():
    pizza=pizza_var.get()
    quantity=spin.get()
    s=size.get()
    toppings=[]
    drink=drink_var.get()
    if pepperoni.get(): toppings.append("pepperoni")
    if mushrooms.get(): toppings.append("mushrooms")
    if onions.get: toppings.append("onions")
    text=" , ".join(toppings) if toppings else "no extra toppings selected"    
    message = f"{quantity} {s} {pizza} pizza(s) topping(S): {text}, drink: {drink}."

    messagebox.showinfo("order placed",message)
Button(root,text="ORDER",font="roboto 30",background="blue",foreground="red",width=15,height=5, command=order).grid(row=8,column=3)



root.mainloop()