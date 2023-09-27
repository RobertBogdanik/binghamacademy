
import tkinter as tk
from time import sleep

window = tk.Tk()
window.title("Hangman")

canvas = tk.Canvas(window, width=400, height=400)
canvas.grid(row=0, column=0)

canvas.create_line(150, 300, 250, 300, width=5)
canvas.create_line(200, 300, 200, 100, width=5)
canvas.create_line(200, 100, 300, 100, width=5)

WORD = "HANGMAN"
USER = "__N__A_"
kill = 0

text = tk.Label(window, text=USER)
text.grid(row=1, column=0)

container = tk.Frame(window)
container.grid(row=2, column=0)

charString = tk.StringVar()
charEntry = tk.Entry(container, textvariable=charString)
charEntry.grid(row=0, column=0)


def user():
    global kill
    global USER

    if WORD != USER and kill < 8:
        if kill > 7:
            canvas.create_line(300, 100, 300, 50, width=5)
        if kill > 6:
            canvas.create_line(300, 250, 325, 300, width=5)
        if kill > 5:
            canvas.create_line(300, 250, 275, 300, width=5)
        if kill > 4:
            canvas.create_line(300, 200, 300, 250, width=5)
        if kill > 3:
            canvas.create_line(300, 200, 325, 225, width=5)
        if kill > 2:
            canvas.create_line(300, 200, 275, 225, width=5)
        if kill > 1:
            canvas.create_oval(275, 150, 325, 200, width=5)
        if kill > 0:
            canvas.create_line(300, 100, 300, 150, width=5)

        guess = charString.get()
        guess = guess[0]
        guess = guess.upper()
        if guess in WORD:
            for i in range(len(WORD)):
                if guess == WORD[i]:
                    USER = USER[:i] + guess + USER[i + 1:]
        else:
            kill += 1

        text.config(text=USER)
        charString.set("")

        window.update()

        if kill >= 8:
            gameOver(False)

        if WORD == USER:
            gameOver(True)


def gameOver(result):
    window.destroy()
    if result:
        print("You Win!")
    else:
        print("You Lose!")


button = tk.Button(container, text="Send", command=user)
button.grid(row=0, column=1)

# window.after(1000, user)
window.mainloop()


