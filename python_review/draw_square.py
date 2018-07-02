import turtle 


def draw_s(some_turtle):
	for i in range(4):
		some_turtle.forward(200)
		some_turtle.right(90)

def draw():
	window = turtle.Screen()
	window.bgcolor("purple")

	jem = turtle.Turtle()
	jem.color("yellow")
	jem.speed(5)
	# draw square 
	jem.begin_fill()
	draw_s(jem)
	jem.end_fill()
    #draw circle
	rose = turtle.Turtle()
	rose.shape("turtle")
	rose.color("pink")
	rose.begin_fill()
	rose.circle(100)
	rose.end_fill()


	# draw traingle 

	brad = turtle.Turtle()
	brad.penup()
	brad.right(90)
	brad.forward(100)
	brad.pendown()
	brad.color("white")
	brad.begin_fill()
	brad.right(45)
	brad.forward(200)
	brad.right(-45)
	brad.backward(145)
	brad.right(-90)
	brad.forward(150)
	brad.end_fill()





	window.exitonclick()



draw()



