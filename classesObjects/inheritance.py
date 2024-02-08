class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#this exactly starts the inheritance
class Student(Person):
  pass


ivan = Student("Ivan","ORSO")

ivan.printname()