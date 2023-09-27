import tkinter
import tkinter.ttk as ttk
from tkinter import filedialog


class TextScrollCombo(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_propagate(False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.txt = tkinter.Text(self)
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set


main_window = tkinter.Tk()

combo = TextScrollCombo(main_window)
# combo.pack(fill="both", expand=True)
combo.config(width=340, height=200)
combo.grid(row=0, column=0, sticky="nsew")

combo.txt.config(font=("consolas", 12), undo=True, wrap='word')
combo.txt.config(borderwidth=3, relief="sunken")

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
    words = text.split()
    distinctWords = set(words)

    combo.txt.delete(1.0, tkinter.END)
    for word in distinctWords:
        combo.txt.insert(tkinter.END, f"{word}\n")

    # letters = [0] * 26
    # for letter in text:
    #     if letter.isalpha():
    #         letters[ord(letter.lower()) - 97] += 1
    # file.close()
    # combo.txt.delete(1.0, tkinter.END)
    # for i in range(26):
    #     combo.txt.insert(tkinter.END, f"{chr(i + 97)}: {letters[i]}\n")


tkinter.Button(bottom_frame, text="Browse", command=browse).grid(row=1, column=2, sticky=tkinter.W)
tkinter.Button(bottom_frame, text="Show Result", command=showResults).grid(row=1, column=3, sticky=tkinter.W)
bottom_frame.grid(row=1, column=0, sticky=tkinter.W)

style = ttk.Style()
style.theme_use('clam')

main_window.mainloop()
