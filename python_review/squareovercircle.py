import turtle

def draw_s(some_turtle):
	for i in range(4):
		some_turtle.forward(150)
		some_turtle.right(90)
def draw_art():
	window = turtle.Screen()
	window.bgcolor('#212121')

	juli = turtle.Turtle()
	juli.color('#FFFF00')
	juli.shape('turtle')
	juli.pensize(2)
	juli.speed(100)
	draw_s(juli)
	for i in range(60):
		draw_s(juli)
		juli.right(6)		
	window.exitonclick()
draw_art()
  