import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()

canvas.create_rectangle(50, 10, 150, 50, fill="white", outline="black")


def move(event):
    canvas.delete("all")
    canvas.create_rectangle(50, 10, 150, 50, fill="white", outline="black")
    if 150 > event.x > 50 > event.y > 10:
        canvas.create_text(event.x, event.y, text="Mouse pointer is inside the rectangle")
    else:
        canvas.create_text(event.x, event.y, text="Mouse pointer is outside the rectangle")


canvas.bind("<B1-Motion>", move)

window.mainloop()
