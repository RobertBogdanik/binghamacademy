import turtle

x, y = eval(input("Enter the center of the circle x, y: "))
width = eval(input("Enter the width of the rectangle: "))
height = eval(input("Enter the height of the rectangle: "))

turtle.penup()
turtle.goto(x-(width/2), y+(height/2))
turtle.pendown()

turtle.forward(width)
turtle.right(90)
turtle.forward(height)
turtle.right(90)
turtle.forward(width)
turtle.right(90)
turtle.forward(height)

turtle.mainloop()
