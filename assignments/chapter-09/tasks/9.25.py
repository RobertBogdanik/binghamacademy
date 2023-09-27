# graw trafic light

import tkinter as tk

window = tk.Tk()

window.geometry("400x500")

canvas = tk.Canvas(window, width=400, height=400)

canvas.create_rectangle(150, 50, 250, 350, fill="black", outline="black")
canvas.create_oval(150, 50, 250, 150, fill="red", outline="red")
canvas.create_oval(150, 150, 250, 250, fill="", outline="yellow")
canvas.create_oval(150, 250, 250, 350, fill="", outline="green")

canvas.pack()

frame = tk.Frame(window)
radio = tk.IntVar()
radio.set(1)


def changeLight():
    canvas.delete("all")
    canvas.create_rectangle(150, 50, 250, 350, fill="black", outline="black")
    if radio.get() == 1:
        canvas.create_oval(150, 50, 250, 150, fill="red", outline="red")
        canvas.create_oval(150, 150, 250, 250, fill="", outline="yellow")
        canvas.create_oval(150, 250, 250, 350, fill="", outline="green")
    elif radio.get() == 2:
        canvas.create_oval(150, 50, 250, 150, fill="", outline="red")
        canvas.create_oval(150, 150, 250, 250, fill="yellow", outline="yellow")
        canvas.create_oval(150, 250, 250, 350, fill="", outline="green")
    elif radio.get() == 3:
        canvas.create_oval(150, 50, 250, 150, fill="", outline="red")
        canvas.create_oval(150, 150, 250, 250, fill="", outline="yellow")
        canvas.create_oval(150, 250, 250, 350, fill="green", outline="green")


radio1 = tk.Radiobutton(frame, text="Red", variable=radio, value=1, command=changeLight)
radio2 = tk.Radiobutton(frame, text="Yellow", variable=radio, value=2, command=changeLight)
radio3 = tk.Radiobutton(frame, text="Green", variable=radio, value=3, command=changeLight)

radio1.pack(side="left")
radio2.pack(side="left")
radio3.pack(side="left")
frame.pack()


window.mainloop()
