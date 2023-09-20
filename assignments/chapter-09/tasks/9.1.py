##############################################
#                                            #
# Author: Robert Bogdanik                    #
# Created Date: 09/20/2023                   #
# Filename: 9.1.py                           #
# License: Apache 2.0                        #
#                                            #
##############################################

import tkinter as tk

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 3
        self.dx = 2
        self.dy = 2
        self.color = "red"

class Panel:
    def __init__(self):
        self.width = 300
        self.height = 200
        self.ball = Ball()
        self.window = tk.Tk()
        self.window.title("Move the Ball")
        self.canvas = tk.Canvas(self.window, bg = "white", width = self.width, height = self.height)
        self.canvas.pack()
        self.canvas.bind("<Key>", self.processKeyEvent)
        self.canvas.focus_set()
        self.displayBall()
        self.window.mainloop()

    def displayBall(self):
        self.canvas.delete("ball")
        self.canvas.create_oval(self.ball.x - self.ball.radius, self.ball.y - self.ball.radius, self.ball.x + self.ball.radius, self.ball.y + self.ball.radius, fill = self.ball.color, tags = "ball")

    def processKeyEvent(self, event):
        if event.keysym == "Up":
            if self.ball.y - self.ball.radius > 0:
                self.ball.y -= self.ball.dy
        elif event.keysym == "Down":
            if self.ball.y + self.ball.radius < self.height:
                self.ball.y += self.ball.dy
        elif event.keysym == "Left":
            if self.ball.x - self.ball.radius > 0:
                self.ball.x -= self.ball.dx
        elif event.keysym == "Right":
            if self.ball.x + self.ball.radius < self.width:
                self.ball.x += self.ball.dx
        self.displayBall()


panel = Panel()
