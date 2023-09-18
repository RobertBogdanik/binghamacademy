import turtle

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.goto(50, 25)
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.penup()
turtle.goto(-50, 25)
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()


turtle.penup()
turtle.goto(-50, -65)
turtle.pendown()
turtle.right(20)
turtle.forward(50)
turtle.left(40)
turtle.forward(50)
turtle.right(20)


turtle.penup()
turtle.goto(-35, -55)
turtle.pendown()
turtle.left(60)
turtle.forward(70)
turtle.right(120)
turtle.forward(70)


turtle.mainloop()
