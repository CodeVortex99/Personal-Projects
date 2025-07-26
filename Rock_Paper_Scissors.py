import tkinter as tk
from functools import partial
from tkinter import messagebox
from tkinter import *
import random as R

root = tk.Tk() # Create a window
root.geometry("300x300") # Set the size of the window
root.title("Rock_Paper_Scissors") # Set the title of the window

frame = tk.Frame(root, padx=20, pady=20, bg="light grey", bd=2) #Create a frame with padding
frame.pack(expand=True, fill='both') # Pack the frame into the window

welcome = Label(frame, text="Welcome to the game of Rock-Paper-Scissors", background="black", foreground="white")
welcome.grid(row=0, column=0, columnspan=2, padx=5, pady=5) # Position the label in the frame
