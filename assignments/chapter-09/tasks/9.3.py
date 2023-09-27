from tkinter import *

FigureFrame = Frame()
FigureFrame.pack()

canvas = Canvas(FigureFrame, width=200, height=100)
canvas.pack()

canvas.create_oval(10, 10, 190, 90, tags="shape")


def draw():
    canvas.delete("shape")
    if v.get() == 1:
        canvas.create_rectangle(10, 10, 190, 90, tags="shape", fill="red" if c.get() == 1 else "")
    elif v.get() == 2:
        canvas.create_oval(10, 10, 190, 90, tags="shape", fill="red" if c.get() == 1 else "")


frame = Frame()
v = IntVar()
c = IntVar()
radio1 = Radiobutton(frame, text="Circle", variable=v, value=1, command=draw)
radio2 = Radiobutton(frame, text="Rectangle", variable=v, value=2, command=draw)

radio1.grid(row=0, column=0)
radio2.grid(row=0, column=1)

checkbox = Checkbutton(frame, text="Filled", command=draw, variable=c)
checkbox.grid(row=0, column=2)

frame.pack()

frame.mainloop()