from tkinter import*

root=Tk()
root.geometry=("300x150")

w=Label(root,text="Choacalate and Ice Creams")

#first frame
frame=Frame(root)
frame.pack()
#second frame
bottom_frame=Frame(root)
bottom_frame.pack(side=BOTTOM)

b1=Button(frame,text="Choco",fg="red",bg="beige")
b1.pack(side=LEFT) 

b2=Button(frame,text="Dark Choco",fg="brown",bg="beige")
b2.pack(side=LEFT) 

b3=Button(frame,text="White Choco",fg="White",bg="beige")
b3.pack(side=LEFT) 

b4=Button(bottom_frame,text="Vanilla",fg="yellow",bg="red")
b4.pack(side=BOTTOM)

b5=Button(bottom_frame,text="Strawberry",fg="pink",bg="red")
b5.pack(side=BOTTOM)

b5=Button(bottom_frame,text="Caramel",fg="yellow",bg="brown")
b5.pack(side=BOTTOM)

root.mainloop()