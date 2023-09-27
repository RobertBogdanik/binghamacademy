import tkinter as tk

circles = 1

window = tk.Tk()
window.geometry("400x400")

canvas = tk.Canvas(window, width=400, height=400)


def change(event):
    canvas.delete("all")
    global circles
    if event.num == 1:
        circles += 1
    elif event.num == 3:
        circles -= 1
    for x in range(circles):
    #     bace on center
        canvas.create_oval(200-(x*10), 200-(x*10), 200+(x*10), 200+(x*10))

    window.update()


canvas.pack()
window.bind("<Button-1>", change)
window.bind("<Button-3>", change)

window.mainloop()
