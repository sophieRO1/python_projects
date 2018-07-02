import turtle


def draw_r(turtle, size, small_angle):
	for i in range(2):
	    turtle.forward(size)
	    turtle.right(small_angle)
	    turtle.forward(size)
	    turtle.right((360-2*small_angle)//2)

def draw_rose(turtle, size, angle):
	for i in range(360//angle):
		draw_r(turtle, size, 60)
		turtle.right(angle)
	turtle.right(90)
	turtle.forward(size*3)



window = turtle.Screen()
window.bgcolor("#FF4081")

jem = turtle.Turtle()
jem.color("yellow")
jem.speed(6)


window.exitonclick()


draw_rose(jem, 100, 5)

