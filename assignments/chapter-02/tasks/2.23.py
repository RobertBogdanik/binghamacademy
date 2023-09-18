import turtle

radius = eval(input("Enter the radius: "))
turtle.penup()
turtle.goto(radius, -radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius, -radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius, radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius, radius)
turtle.pendown()
turtle.circle(radius)

turtle.mainloop()
