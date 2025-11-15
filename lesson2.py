import tkinter as tk

root = tk.Tk()
root.title("Login Me!!!!")
root.geometry("200x200")
root.config(background="blue")

#label for username
user_name=tk.Label(root,text="Username").place(x=40,y=60)
#label for password
user_password=tk.Label(root,text="Password").place(x=40,y=100)
#entry for username
user_name_entry=tk.Entry(root,width=30).place(x=110,y=60)
#entry for password
user_password_entry=tk.Entry(root,show="*",width=30).place(x=110,y=100)
#submit button
submit_button=tk.Button(root,text="Submit",command=root.destroy).place(x=80,y=140)

root.mainloop()