# draw sinus function

import turtle
import math

turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.goto(200, 0)
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.goto(0, -200)
turtle.penup()
turtle.goto(-176, 50 * math.sin((-176 / 100) * 2 * math.pi))
for x in range(-175, 176):
    turtle.pendown()
    turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))

turtle.mainloop()
