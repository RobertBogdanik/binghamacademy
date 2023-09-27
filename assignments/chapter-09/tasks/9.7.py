from tkinter import *

window = Tk()

canvas = Canvas(window, width=300, height=300)

for i in range(8):
    canvas.create_line(0, 300 / 8 * i, 300, 300 / 8 * i)

for i in range(8):
    canvas.create_line(300 / 8 * i, 0, 300 / 8 * i, 300)

canvas.pack()
window.mainloop()
