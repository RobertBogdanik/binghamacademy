import turtle


turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(0, 90)
turtle.goto(0, 0)
turtle.goto(75, 0)
turtle.goto(0, 0)
turtle.left(90)
turtle.left(90-(0.5*15))
turtle.forward(60)

turtle.penup()

turtle.goto(-5, 85)
turtle.write("12")
turtle.goto(0, -100)
turtle.write("6")
turtle.goto(90, -5)
turtle.write("3")
turtle.goto(-90, -5)
turtle.write("9")
turtle.goto(-15, -120)
turtle.write("9:15:00")

turtle.mainloop()
