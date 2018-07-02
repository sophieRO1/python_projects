import turtle


window = turtle.Screen()
window.bgcolor("#212121")


turtle.speed(100)

for i in range(100):
	turtle.color("#BA68C8")
	turtle.circle(1*i)
	turtle.circle(-1*i)
	turtle.left(i)
	
window.exitonclick()
