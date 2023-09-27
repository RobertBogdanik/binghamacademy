import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

label = tk.Label(window, text="Programming is fun")
label.pack(side="top", fill="both", expand=True)


def click(event):
    label.configure(text=f"({event.x}, {event.y})")
    label.place(x=event.x, y=event.y)


window.bind("<Button-1>", click)
window.bind("<Button-3>", click)


window.mainloop()