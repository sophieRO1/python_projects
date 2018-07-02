import turtle

def draw_s(some_turtle):
	for i in range(4):
		some_turtle.forward(100)
		some_turtle.right(90)



def draw():
	window = turtle.Screen()
	window.bgcolor('pink')


	brad = turtle.Turtle()
	brad.color('black')
	brad.speed(2)
	for i in range(100):
		draw_s(brad)
		brad.fill('white')
		brad.right(10)
		brad.right(-30)
		brad.color('yellow')
	

	window.exitonclick()

draw()











