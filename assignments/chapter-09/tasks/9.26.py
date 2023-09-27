import tkinter as tk
import random

window = tk.Tk()
window.geometry("400x400")

canvas = tk.Canvas(window, width=400, height=350)


def display():
    canvas.delete("all")
    for ball in range(10):
        x = random.randint(0, 400)
        y = random.randint(0, 350)

        canvas.create_oval(x, y, x+20, y+20, fill="black")
    window.update()


canvas.pack()

button = tk.Button(window, text="Dispaly", command=display)
button.pack()

window.mainloop()
