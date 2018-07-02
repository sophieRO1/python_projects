import turtle

window = turtle.Screen()
window.bgcolor('pink')

for i in range(100):
	brad = turtle.Turtle()
	brad.color('white')
	brad.speed(100)

	brad.circle(3*i)
	brad.circle(-3*i)
	brad.left(i)

	



window.exitonclick()