from turtle import*

speed(0)
bgcolor('black')
pencolor('violet')
hideturtle()

for i in range(155):
    right(i)
    circle(170,i)
    fd(i)
    right(90)

    exitonclick()
