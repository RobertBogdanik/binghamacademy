import tkinter as tk

window = tk.Tk()

# displays a still fan
canvas = tk.Canvas(window, width=300, height=300)

canvas.create_arc(30, 50, 230, 250, start = 0, extent = 30, outline = "green", fill = "red", width = 2)
canvas.create_arc(30, 50, 230, 250, start = 90, extent = 30, outline = "green", fill = "red", width = 2)
canvas.create_arc(30, 50, 230, 250, start = 180, extent = 30, outline = "green", fill = "red", width = 2)
canvas.create_arc(30, 50, 230, 250, start = 270, extent = 30, outline = "green", fill = "red", width = 2)

canvas.pack()


degree = 0


def rotate():
    global degree
    canvas.delete("all")
    canvas.create_arc(30, 50, 230, 250, start = degree, extent = 30, outline = "green", fill = "red", width = 2)
    canvas.create_arc(30, 50, 230, 250, start = degree + 90, extent = 30, outline = "green", fill = "red", width = 2)
    canvas.create_arc(30, 50, 230, 250, start = degree + 180, extent = 30, outline = "green", fill = "red", width = 2)
    canvas.create_arc(30, 50, 230, 250, start = degree + 270, extent = 30, outline = "green", fill = "red", width = 2)
    degree += 5
    window.after(100, rotate)
    window.update()


rotate()

window.mainloop()
