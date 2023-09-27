import tkinter as tk

# MAKE LATER

window = tk.Tk()

top = tk.Frame(window)
top.pack(side="top", fill="both", expand=True)

middle = tk.Frame(window)
middle.pack(side="top", fill="both", expand=True)

bottom = tk.Frame(window)

# add 5 radio to top
radio1 = tk.Radiobutton(top, text="Red", value=1)
radio2 = tk.Radiobutton(top, text="Green", value=2)
radio3 = tk.Radiobutton(top, text="Blue", value=3)
radio4 = tk.Radiobutton(top, text="Yellow", value=4)
radio5 = tk.Radiobutton(top, text="Black", value=5)

radio1.pack(side="left")
radio2.pack(side="left")
radio3.pack(side="left")
radio4.pack(side="left")
radio5.pack(side="left")

x = tk.IntVar()
x.set(200)

label = tk.Label(middle, text="Welcome")
label.pack(side="top", fill="both", expand=True)


button1 = tk.Button(bottom, text="<=", command=lambda: x.set(x.get() + 10))
button2 = tk.Button(bottom, text="=>", command=lambda: x.set(x.get() - 10))
button1.pack(side="left")
button2.pack(side="left")

bottom.pack(fill="both", expand=True)

# on x change, change label text
def changeLabel():
    pass

changeLabel()






window.mainloop()