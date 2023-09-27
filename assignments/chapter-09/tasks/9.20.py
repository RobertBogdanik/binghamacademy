import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()

canvas.create_oval(50, 10, 150, 110, fill="white", outline="black")


def mouse(event):
    canvas.delete("all")
    canvas.create_oval(50, 10, 150, 110, fill="white", outline="black")
    if (event.x - 100)**2 + (event.y - 60)**2 < 50**2:
        canvas.create_text(event.x, event.y, text="Mouse pointer is inside the circle")
    else:
        canvas.create_text(event.x, event.y, text="Mouse pointer is outside the circle")


canvas.bind("<B1-Motion>", mouse)

window.mainloop()
