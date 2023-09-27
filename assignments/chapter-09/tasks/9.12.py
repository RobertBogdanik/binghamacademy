import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

label = tk.Label(window, text="Programming is fun")
label.pack(side="top", fill="both", expand=True)


def click(event):
    if event.num == 1:
        label.configure(text="It is fun to program")
    elif event.num == 3:
        label.configure(text="Programming is fun")


window.bind("<Button-1>", click)
window.bind("<Button-3>", click)


window.mainloop()