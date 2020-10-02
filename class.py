class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def sit(self):
    #Ininitalize name and age attributes
    print(f"{self.name} is now sitting.")
    
  def roll_over(self):
    #Simulate rolling over in response to a command
    print(f"{self.name} rolled over!")
