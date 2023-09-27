import tkinter
import tkinter.ttk as ttk
from tkinter import filedialog
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

main_window = tkinter.Tk()

bottom_frame = tkinter.Frame(main_window, width=600, height=100)
tkinter.Label(bottom_frame, text="Enter a filename: ").grid(row=1, column=0, sticky=tkinter.W)
filename = tkinter.StringVar()
tkinter.Entry(bottom_frame, textvariable=filename, width=20).grid(row=1, column=1, sticky=tkinter.W)


def browse():
    pass
    filename.set(filedialog.askopenfilename())


def showResults():
    file = open(filename.get(), "r")
    text = file.read()
    letters = [0] * 26
    for letter in text:
        if letter.isalpha():
            letters[ord(letter.lower()) - 97] += 1
    file.close()

    data = letters
    labels = [chr(i + 97) for i in range(26)]
    fig = Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).bar(labels, data)
    canvas = FigureCanvasTkAgg(fig, master=main_window)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")


tkinter.Button(bottom_frame, text="Browse", command=browse).grid(row=1, column=2, sticky=tkinter.W)
tkinter.Button(bottom_frame, text="Show Result", command=showResults).grid(row=1, column=3, sticky=tkinter.W)
bottom_frame.grid(row=1, column=0, sticky=tkinter.W)

style = ttk.Style()
style.theme_use('clam')

main_window.mainloop()
