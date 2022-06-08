class Animal_Kingdom():
	def __init__(self, SpeciesName, ClassName):
		self.SpeciesName = SpeciesName
		self.ClassName = ClassName
	def get_SpeciesName(self):
		return self.SpeciesName

	def get_ClassName(self):
		return self.ClassName   

	def display(self):
		print("Animal Kingdom Name is: " + self.SpeciesName)

    

class Invertebrates(Animal_Kingdom):
	def __init__(self, SpeciesName, ClassName, Aquatic):
		Animal_Kingdom.__init__(self, SpeciesName, ClassName)
		self.Aquatic = Aquatic
		self.ClassName= ClassName


	def get_Species_Name(self):
		return self.SpeciesName

	def get_Class_Name(self):
		return self.ClassName   

	def display(self):
		Animal_Kingdom.display(self)
		print("******************************************whether it is Aquatic: {},\n and its class is {} ".format(self.Aquatic,self.ClassName))
    

    
class Vertebrates(Animal_Kingdom):
	def __init__(self, SpeciesName, ClassName,fly):
		Animal_Kingdom.__init__(self, SpeciesName, ClassName )
		self.fly = fly
		self.ClassName= ClassName

	def get_SpeciesName(self):
		return self.SpeciesName

	def get_ClassName(self):
		return self.ClassName   

	def display(self):
		Animal_Kingdom.display(self)
		print("***********************************\nWhether can it Fly: {},\n and its class is: ".format(self.fly,self.ClassName))



class Type():
	@classmethod
	def as_Vertebrates(self, SpeciesName, ClassName, fly):
		return Vertebrates(SpeciesName,ClassName, fly)

	@classmethod

	def as_Invertebrates(self, SpeciesName, ClassName, Aquatic):
		return Invertebrates(SpeciesName, ClassName,Aquatic)

# these are mostly aquatic with no backbone and simple structure
#Vertebrates1 = Type.as_Vertebrates("Snail","Gastropoda","NO")
#Vertebrates1.display()
# these are mostly with with backbone and complext strucutre
#Invertebrates1 = Type.as_Invertebrates("Black Panther","Mammalia","NO")
#Invertebrates1.display()

data_of_invertibrates = {}
data_of_vertibrates = {}

while True:
	try:
		print("exit: 0")
		data = str(input("enter whether the animal is invertebrate or vertebrate....\n"))
		if data == "invertebrate":
			print("****************\n1.add information")
			print("2.view information")
			print("3.update informationo")
			choice =  int(input("Select Your Choice "))
			if choice == 1:
				name = str(input("Enter Species name : "))
				data_of_invertibrates[name] = Type.as_Invertebrates(name, 
					str(input("Enter Class Name : ")), 
					str(input("Enter whether it is Aqutic or not  : ")), 
				)
			elif choice == 2:
				data_of_invertibrates[str(input("Enter Species name: "))].display()

			elif choice == 3:
				name = str(input("Enter Species name: "))
				data_of_invertibrates.pop(name)
				data_of_invertibrates[name] = Type.as_Invertebrates(name, 
					str(input("Enter Class Name : ")), 
					str(input("Enter whether it is Aqutic or not  : "))
				)
    
			else:
				print("Please Select Proper Choice ..!!!")

		elif data == "vertebrate":
			print("*****************\n1.add information")
			print("2.view information")
			print("3.update information")
			choice =  int(input("Enter Choice "))
			if choice == 1:
				name = str(input("Enter Species name : "))
				data_of_vertibrates[name] = Type.as_Vertebrates(name, 
					str(input("Enter Class Name : ")), 
					str(input("Enter whether it is Aqutic or not  : ")), 
				)
			elif choice == 2:
				data_of_vertibrates[str(input("Enter Species name : "))].display()
			
			elif choice == 3:
				name = str(input("Enter Species name : "))
				data_of_vertibrates.pop(name)
				data_of_vertibrates[name] = Type.as_Vertebrates(name, 
					str(input("Enter Class Name : ")), 
					str(input("Enter whether it is Aqutic or not  : ")), 
				)

			else:
				print("enter valid details")

		elif data == "0":
			break

		else:
			print("enter valid details")
	except Exception as e:
		print(e)
		print("Invalid Data Format")

