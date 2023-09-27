from tkinter import *

canvas = Canvas(width=600, height=400)

for i in range(20):
    canvas.create_rectangle(10 + i * 10, 10 + i * 10, 590 - i * 10, 390 - i * 10)

canvas.pack()
mainloop()
