class Parent():
	def __init__(self, last_name, eye_color):
		print "Parent constructor called  "
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		return "last name is:"+ self.last_name


class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		print "child constructor called"
		Parent.__init__(self,last_name, eye_color)
		self.number_of_toys = number_of_toys

	def show_info(self):
		print "last name is:"+ self.last_name
		print "eye_color is:"+ self.eye_color
		print 'number of toys is :' + str(self.number_of_toys)
	


# koko = Parent("koko", "blue")
# print koko.eye_color

milry = Child("milry", "blue", 2)
# print milry.number_of_toys
print milry.show_info()
