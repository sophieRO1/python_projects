import turtle

window = turtle.Screen()
window.bgcolor("#000000")

turtle.speed(100)
for i in range(100):
	turtle.color("#1DE9B6")
	
	turtle.circle(1*i)
	turtle.circle(-1*i)
	turtle.left(120)
	

window.exitonclick()