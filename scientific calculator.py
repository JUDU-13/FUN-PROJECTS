import tkinter as tk
from math import *

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")

def clear():
    entry.delete(0,tk.END)

root = tk.Tk()
root.geometry("250x300")
root.title("Scientific Calculator")
root.configure(bg = '#3c3f41')

entry = tk.Entry(root,bg = '#dfe6e9', fg = '#2d3436', font=("Helvetica", 14))
entry.place(relx = 0.5, rely = 0.1, anchor = tk.CENTER)

button_frame = tk.Frame(root,bg = '#3c3f41')
button_frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

button_list = [
    "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*",
    ".", "/", "0", "C", "(", ")", "=", "sin", "cos", "tan", "log", "ln", "sqrt"
]

r = 1
c = 0

for button_text in button_list:
    command = lambda x=button_text: entry.insert(tk.END,x)
    tk.Button(button_frame, text = button_text, width = 5, height = 2, bg = "#636e72",fg = '#f1c40f', font=("Helvetica", 14), command = command).grid(row = r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

tk.Button(button_frame, text = "=", width = 5, height = 2, bg = "#636e72",fg = '#f1c40f', font=("Helvetica", 14), command = calculate).grid(row = r, column = 0, columnspan = 4)
tk.Button(button_frame, text = "C", width = 5, height = 2, bg = "#636e72",fg = '#f1c40f', font=("Helvetica", 14), command = clear).grid(row = r, column = 4)

root.mainloop()
