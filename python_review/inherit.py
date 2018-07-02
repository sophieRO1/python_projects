class Parent():
	def __init__(self, last_name,eye_color,  age):
		print ("Parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color
		self.age = age

	def show_info(self):
		print ("the last name : "+ self.last_name)
		print ("eye color:  " +self.eye_color)
		print ("the age is " + str(self.age ))


class Child(Parent):
	def __init__(self, last_name, eye_color,age , number_of_toys):
		#print ("Child constructor called")
		Parent.__init__(self, last_name, eye_color, age)
		self.number_of_toys = number_of_toys

	def show_info(self):
		print ("the last name : "+ self.last_name)
		print ("eye color:  " +self.eye_color)
		print ("the age is " + str(self.age ))
		print ("the number of toys :"+str(self.number_of_toys))


koko = Parent("koko", "blue", 2)
#print koko.eye_color
jojo = Child("JOJO", "Green", 1 , 4)
# print jojo.last_name
# print jojo.number_of_toys
#koko.show_info()
jojo.show_info()