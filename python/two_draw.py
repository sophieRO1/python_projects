import turtle


def draw_ss(some_turtle):
	for i in range(1, 5):
		some_turtle.forward(100)
		some_turtle.right(90)
	

	



def art():
	window = turtle.Screen()
	window.bgcolor('yellow')

	# create brad 

	brad = turtle.Turtle()
	brad.color('black')
	brad.shape('arrow')
	brad.speed(2)
	draw_ss(brad)
	

    

    # angie 

    koko = turtle.Turtle()
    koko.circle(90)


	window.exitonclick()

art()














