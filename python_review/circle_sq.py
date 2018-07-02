import turtle


def draw_s(some_turtle):
	for i in range(4):
		some_turtle.forward(110)
		some_turtle.right(90)

def draw():

	window = turtle.Screen()
	window.bgcolor("black")

	brad = turtle.Turtle()
	brad.speed(10)
	brad.shape("arrow")
	brad.pensize(2)
	brad.color("#8C9EFF")
	draw_s(brad)
	for i in range(36):
		draw_s(brad)
		brad.right(10)



	window.exitonclick()

draw()