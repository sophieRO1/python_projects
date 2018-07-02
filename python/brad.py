import turtle


def draw_s():
    window = turtle.Screen()
    window.bgcolor('red')



    brad = turtle.Turtle()
    # brad.forward(100)
    # brad.right(90)
    # brad.forward(100)
    # brad.right(90)
    # brad.forward(100)
    # brad.right(90)
    # brad.forward(100)
    # brad.right(90)

    brad.shape('circle')
    brad.circle(50)
    brad.color('pink')
    brad.speed(2)
    brad.forward(100)
    brad.circle(50)
    brad.color('white')	
    brad.speed(4)
    brad.right(90)
    brad.forward(100)
    brad.left(90)
    brad.circle(50)
    brad.color('pink')


    window.exitonclick()



draw_s()
