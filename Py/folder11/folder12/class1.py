from folder21.folder22.folder23.class2 import Class2

class Class1:
	connection = "DoneClass1"
	
	def __init__(self):
		x = Class2()
		self.connection = x.connection
		

x = Class1()
print(x.connection)
