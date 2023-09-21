import tkinter as tk
from  tkinter import ttk

root = tk.Tk()
root.title("entry")

label_name = tk.Label(text = "ユーザー名")
entry_name = tk.Entry()
label_name.grid(row=0,column=0)
entry_name.grid(row=0,column=1)

label_password = tk.Label(text = "パスワード")
entry_password = tk.Entry(show="●")
label_password.grid(row=1, column=0)
entry_password.grid(row=1, column=1)

def get_data():
    id = entry_name.get()
    password = entry_password.get()
    print("ユーザー名:", id)
    print("パスワード:", password)

button_ok = tk.Button(text="OK", command=get_data)
button_quit = tk.Button(text="Quit", command=quit)
button_ok.grid(row=2, column=0)
button_quit.grid(row=2, column=1)

root.mainloop()
