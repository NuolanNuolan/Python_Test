
def make_pizza(size,*toppings):
	name = size
	for topping in toppings:
		name = name + topping
	return name


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print("sit down %s-----%s"%(self.name,self.age))
    def changeage(self,age):
    	self.age += age


class battery():
	def __init__(self, battery_size=70):

		self.battery_size = battery_size
	def describe_battery(self):
		print('this is message')

class electri(Dog):
	def __init__(self, name, age):
		super().__init__(name, age)
		self.battery_size = battery()
	def sit(self):	
		print("I am son")
		
