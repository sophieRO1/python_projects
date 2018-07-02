import turtle

def draw_square(some_turtle):
	for i in range(0, 4):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("#000000")
    # first object or instance
	ronda = turtle.Turtle()
	ronda.shape("arrow")
	ronda.speed(20)
	ronda.color("#AD1457")
	# draw square
	ronda.begin_fill()
	draw_square(ronda)
	ronda.end_fill()
    #  second object or instance
	jem = turtle.Turtle()
	jem.color("#EC407A")
	jem.begin_fill()
	# draw circle
	jem.circle(60)
	jem.end_fill()
	# third object or instance
	rima = turtle.Turtle()
	rima.color("#C0CA33")
	rima.penup()
	rima.right(90)
	rima.forward(100)
	rima.pendown()
	rima.begin_fill()
	## draw triangle
	rima.forward(100)
	rima.right(90)
	rima.forward(150)
	rima.left(33)
	rima.back(180)
	rima.end_fill()

	window.exitonclick()

draw_art()