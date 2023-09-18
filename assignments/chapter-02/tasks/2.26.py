import turtle
import math

x, y = eval(input("Enter the center of the circle x, y: "))
radius = eval(input("Enter the radius of the circle: "))
turtle.penup()
turtle.goto(x, y-radius)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write(radius**2*math.pi)
turtle.mainloop()