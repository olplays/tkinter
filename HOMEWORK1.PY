import tkinter as tk

root = tk.Tk()
root.title("Login Me!!!!")
root.geometry("200x200")
root.config(background="blue")

#label for username
email_label=tk.Label(root,text="Email").place(x=40,y=60)

#entry for username
user_name_entry=tk.Entry(root,width=30).place(x=110,y=60)

#label for password
password_label=tk.Label(root,text="Password").place(x=40,y=100)

#entry for password
user_password_entry=tk.Entry(root,show="*",width=30).place(x=110,y=100)

#food label
food_label=tk.Label(root,text="What food would you like?").place(x=40,y=140)

#food entry
food_entry=tk.Entry(root,width=30).place(x=110,y=170)

#drink label
drink_label=tk.Label(root,text="What drink would you like?").place(x=40,y=200)

#drink entry
drink_entry=tk.Entry(root,width=30).place(x=110,y=230)

#dessert label
dessert_label=tk.Label(root,text="What dessert would you like?").place(x=40,y=260)

#dessert entry
dessert_entry=tk.Entry(root,width=30).place(x=110,y=290)

#submit button
submit_button=tk.Button(root,text="Submit",command=root.destroy).place(x=80,y=340)

root.mainloop()