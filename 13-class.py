class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hi " + self.name + ", Welcome to the world of Python.")

my_name=str(input("Enter your Name : "))
my_age=int(input("Enter your age : "))
p1 = Person(my_name,my_age)
p1.myfunc()
