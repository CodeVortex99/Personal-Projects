import tkinter as tk
from tkinter import messagebox
from functools import partial
from tkinter import *

root = tk.Tk() # Create a window
root.geometry("300x200") # Set the size of the window
root.title("Unknown") # Set the title of the window

# Create a frame with padding
frame = tk.Frame(root, padx=20, pady=20, bg="light grey", bd=2)
frame.pack(expand=True, fill='both') # Pack the frame into the window

def custom_message(message: str):
    messagebox.showinfo("Title of Messagebox", message)

def clear():
    txt_btn.delete(1.0, END)

# Create buttons with grid positioning
button = tk.Button(frame, text="Click me", 
                  command=partial(custom_message, "Welcome to the world of Python."),
                  fg="black", width=15, borderwidth=3, relief="sunken")
button.grid(row=0, column=0, padx=5, pady=5)

mb_btn = tk.Button(frame, text="Show Message!", 
                  command=partial(custom_message, "You are at the correct place to learn Python!"),
                  fg="black", width=15, borderwidth=3, relief="solid")
mb_btn.grid(row=0, column=1, padx=5, pady=5)

type_btn = tk.Button(frame, text="Text", command=partial(custom_message, "This is being worked on!"), 
                     fg="black", width=15, borderwidth=3, relief="groove")
type_btn.place(x=70, y=50)

txt_btn = Text(frame, width=50, height=15, font="Serif sans, 9")
txt_btn.pack(pady=20)

clr_btn = Button(frame, text="clear", command=clear)
clr_btn.grid(row=0,column=0)

root.mainloop()