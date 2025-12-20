from tkinter import * 
from tkinter import messagebox

root=Tk()
root.geometry("400x400")

label=Label(root,text="Hi I am a message box",font="50")
label.pack()
messagebox.showinfo("Show info","Information")
messagebox.showwarning("Show warning","Warning")
messagebox.showerror("Show error","THERE IS AN ERROR")
messagebox.askquestion("show question","Do you want to proceed")
messagebox.askokcancel("ask ok cancel","are you sure?")
messagebox.askyesno("ask yes no","find the value?")
messagebox.askretrycancel("ask retry cancel","try again?")
root.mainloop()