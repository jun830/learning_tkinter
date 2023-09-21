from random import choice
import tkinter as tk

def dispLabel():
    label.configure(text=choice(["大吉", "中吉","小吉","吉","凶"]))

root = tk.Tk()
root.title("おみくじ")
root.geometry("200x100")

label = tk.Label(root, text="おみくじだよ")
label.pack()

button = tk.Button(root, text="おしてね", command = dispLabel)
button.pack()

root.mainloop()
