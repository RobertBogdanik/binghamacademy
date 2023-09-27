import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

label = tk.Label(window, text="Welcome")
label.pack(side="top", fill="both", expand=True)

status = True

def flash():
    global status
    if status:
        label.configure(text="Welcome")
        status = False
    else:
        label.configure(text="")
        status = True
    window.after(1000, flash)


flash()

window.mainloop()
