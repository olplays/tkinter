from tkinter import*
from tkinter.ttk import*

#create the window
root=Tk()

progress=Progressbar(root,orient=HORIZONTAL,length=100,mode='determinate')

#function to check the updates

def bar():
    import time
    progress["value"]=20
    root.update_idletasks()
    time.sleep(1)

    progress["value"]=40
    root.update_idletasks()
    time.sleep(1)

    progress["value"]=60
    root.update_idletasks()
    time.sleep(1)

    progress["value"]=80
    root.update_idletasks()
    time.sleep(1)

    progress["value"]=100

progress.pack(pady=10)
#add button
button=Button(root,text="Start",command=bar).pack(pady=10)
#add spinbox
w=Spinbox(root,from_=0,to=10)
w.pack()
root.mainloop()
#infinite loop
root.mainloop()