import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

x, y = 300, 300

canvas = tk.Canvas(window, width=x, height=y)


def move(event):
    print(event.keysym)
    global x, y
    if event.keysym == "Up":
        canvas.create_line(x, y, x, y-10)
        y -= 10
    elif event.keysym == "Down":
        canvas.create_line(x, y, x, y+10)
        y += 10
    elif event.keysym == "Left":
        canvas.create_line(x, y, x-10, y)
        x -= 10
    elif event.keysym == "Right":
        canvas.create_line(x, y, x+10, y)
        x += 10

    canvas.pack()
    window.update()




window.bind("<Up>", move)
window.bind("<Down>", move)
window.bind("<Left>", move)
window.bind("<Right>", move)

window.mainloop()
