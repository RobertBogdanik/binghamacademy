import tkinter as tk


window = tk.Tk()

car = tk.Frame(window, width=300, height=300)
car.pack()

canvas = tk.Canvas(car, width=300, height=300)
canvas.pack()


def drawCar(x, y):
    canvas.create_rectangle(x, y-10, x+50, y-20, fill="black")
    canvas.create_oval(x+10, y-10, x+20, y, fill="black")
    canvas.create_oval(x+30, y-10, x+40, y, fill="black")
    canvas.create_polygon(x+10, y-20, x+20, y-30, x+30, y-30, x+40, y-20, fill="black")


x, y = 0, 300
while x < 300:
    canvas.delete("all")
    drawCar(x, y)
    x += 1
    window.after(100, drawCar(x, y))
    window.update()




window.mainloop()