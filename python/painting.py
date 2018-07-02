import turtle

def draw(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

        

def draw_shape():

    window = turtle.Screen()
    window.bgcolor('pink')


    brad = turtle.Turtle()
    brad.color("blue")
    brad.speed(20)
    brad.shape("arrow")
    for i in range(40):
        draw(brad)
        brad.right(10)

  
draw_shape()
