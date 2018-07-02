import turtle

def draw_square(some_turtle):
	
	for i in range(0, 2):
		some_turtle.forward(100)
		some_turtle.right(30)
		some_turtle.forward(100)
		some_turtle.right(150)

def draw_flower():
	window = turtle.Screen()
	window.bgcolor("#000000")

	juli = turtle.Turtle()
	juli.color("#FF1744")
	juli.speed(100)
	juli.shape('triangle')

	for i in range(0, 36):
	    draw_square(juli)
	    juli.right(10)
	for i in range(0, 30):
		juli.circle(20)
		juli.right(90)
		juli.right(10)
	juli.right(-30)
	juli.forward(300)

	window.exitonclick()
draw_flower()
