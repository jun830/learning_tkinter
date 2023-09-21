import tkinter as tk
from  tkinter import ttk

root = tk.Tk()
root.title("はじめてのtkinter")
root.geometry("200x100")

label = ttk.Label(root, text = "Hello Python").pack()

entry = ttk.Entry(root).pack()

button = ttk.Button(root, text = "click").pack()

root.mainloop()
