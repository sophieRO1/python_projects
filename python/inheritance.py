class Parent():
    def __init__(self, last_name, eye_color):
        print 'parent constructor called:'
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print 'last name is:'+self.last_name
        print 'eye color is: '+self.eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, age):
        print 'child constructor called'
        Parent.__init__(self, last_name, eye_color)
        self.age = age
    def show_info(self):
        print 'last name is:'+self.last_name
        print 'eye color is: '+self.eye_color
        print 'age is :'+str(self.age)


#koko = Parent('JOJO', 'blue')
#koko.show_info()

gtgt = Child('fhfhf', 'blue', 2)
gtgt.show_info()
#print gtgt.age
