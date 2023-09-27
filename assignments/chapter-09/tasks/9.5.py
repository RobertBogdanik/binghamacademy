# Write a program that displays a checkerboard in
# which each white and black cell is a canvas with a background of black or white,
# as shown in Figure 9.25a.

from tkinter import *
canvas = Canvas(width = 400, height = 400)

skip = True
for i in range(8):
    for j in range(8):
        if skip:
            skip = False
            continue
        canvas.create_rectangle(50 * i, 50 * j, 50 * (i + 1), 50 * (j + 1), fill = "black")
        skip = True
    if skip:
        skip = False
    else:
        skip = True

canvas.pack()
mainloop()
