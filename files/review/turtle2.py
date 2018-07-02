import turtle

def draw_square(some_turtle):
	for i in range(1, 5):
		some_turtle.forward(100)
		some_turtle.left(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("#000000")

	juli = turtle.Turtle()
	juli.color("#AB47BC")
	juli.speed(20)
	juli.shape('arrow')
	
	# draw circle out of square 
	for i in range(60):
		draw_square(juli)
		juli.right(6)

	window.exitonclick()
draw_art()

  
