from tkinter import *

canvas = Canvas(width=400, height=400)

for i in range(16):
    string = ""
    for j in range(1, 12-i):
        string += str(j)+" "
    canvas.create_text(200, 200 - i*15, text=string)


canvas.pack()
mainloop()
