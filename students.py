class Students:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print("My name is {} and my age is {}".format(self.name, self.age))

student1 = Students("Sam", 19)
student2 = Students("Kara", 22)
#objectname = classname()
#creating an object of a class = instantiation(instantiating a class)
student3 = Students("Barry", 20)
student4 = Students("Oliver", 21)
