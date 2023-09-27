from tkinter import *
from random import randint

# ???????????????

window = Tk()

canvas = Canvas(window, width=300, height=300)
canvas.pack()

for i in range(3):
    for j in range(3):
        if randint(0, 1) == 0:
            canvas.create_image(100 * i + 50, 100 * j + 50, image=PhotoImage(file="o.gif"))
        else:
            canvas.create_image(100 * i + 50, 100 * j + 50, image=PhotoImage(file="x.gif"))

window.mainloop()
