import turtle

len = eval(input("Enter an integer: "))

for x in range(5):
    turtle.right(180-36)
    turtle.forward(len)

turtle.mainloop()