import tkinter as tk

root = tk.Tk() # Create the main window
root.title("My First GUI") # Set the window title
root.geometry("100x100")
button = tk.Button(root, text="Click Me",bd="5",background="cyan",command=root.destroy) # Create a button widget
button.pack(side="top") 

root.mainloop() # Start the GUI event loop