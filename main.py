import tkinter as tk 
from tkinter import messagebox 
 
def on_button_click(symbol):     
    if symbol == "=":         
        try: 
            result = eval(entry_var.get())             
            entry_var.set(result)         
        except Exception as e: 
            messagebox.showerror("Помилка", "Некоректний вираз")     
    elif symbol == "C":         
        entry_var.set("")     
    else: 
        entry_var.set(entry_var.get() + str(symbol)) 
 
root = tk.Tk() 
root.title("Калькулятор") 
 
entry_var = tk.StringVar() 
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief=tk.GROOVE, justify="right") 
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8) 
 
buttons = [ 
    ('7', '8', '9', '/'), 
    ('4', '5', '6', '*'), 
    ('1', '2', '3', '-'), 
    ('0', 'C', '=', '+') 
] 
 
for r, row in enumerate(buttons, 1):     
    for c, symbol in enumerate(row):         
        btn = tk.Button(root, text=symbol, font=("Arial", 20), command=lambda s=symbol: 
        on_button_click(s), width=5, height=2)         
        btn.grid(row=r, column=c, padx=5, pady=5) 
 
root.mainloop() 
