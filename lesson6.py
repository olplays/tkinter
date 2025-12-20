from tkinter import*

window=Tk()
window.title("My favorite dishes")
window.geometry("300x250")
#create a listbox
listbox=Listbox(window,height=10,width=15,bg="grey",activestyle="dotbox",font="roboto",fg="yellow")

label=Label(window,text="Food Items")

#enyer elements into the listbox
listbox.insert(1,"Nachos")
listbox.insert(2,"Sandwich")
listbox.insert(3,"Burger")
listbox.insert(4,"Pizza")
listbox.insert(5,"Fries")

label.pack()
listbox.pack()

scrollbar=Scrollbar(window)
scrollbar.pack(side=RIGHT,fill=Y)

myList=Listbox(window,yscrollcommand=scrollbar.set)
for line in range(1,26):
    myList.insert(END,"HI "+str(line))
myList.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=myList.yview)
window.mainloop()