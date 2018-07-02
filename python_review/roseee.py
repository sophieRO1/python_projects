import turtle 

def draw_r():
    window = turtle.Screen()
    window.bgcolor('black')

    turtle.shape("arrow")
    turtle.speed(200)
    turtle.color('#E91E63')
    for i in range(180):
        for i in range(3):
            turtle.forward(100)
            turtle.right(120)
        turtle.right(2)
    
    turtle.right(90)
    turtle.forward(200)

    window.exitonclick()

draw_r()