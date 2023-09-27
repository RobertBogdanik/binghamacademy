import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

x, y = 200, 200

canvas = tk.Canvas(window, width=400, height=400)


def move(event):
    canvas.delete("all")
    global x, y
    if event.keysym == "Up":
        y -= 10
        canvas.create_oval(x, y, x-20, y-20)
    elif event.keysym == "Down":
        y += 10
        canvas.create_oval(x, y, x-20, y-20)
    elif event.keysym == "Left":
        x -= 10
        canvas.create_oval(x, y, x-20, y-20)
    elif event.keysym == "Right":
        x += 10
        canvas.create_oval(x, y, x-20, y-20)

    window.update()


canvas.create_oval(x, y, x-20, y-20)
canvas.pack()
window.bind("<Up>", move)
window.bind("<Down>", move)
window.bind("<Left>", move)
window.bind("<Right>", move)

window.mainloop()
