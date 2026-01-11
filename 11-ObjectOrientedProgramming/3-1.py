#The __str__() method should return a string that is a readable or meaningful
#representation of the object. It is mainly used for displaying the object to users.
 #  When you pass the object to str() or print(),
#Python internally calls __str__() to get a string representation of the object.
#Look at the example below. 
#Then run this program.

class Car:
   def __init__(self, brand, model, year):
      self.brand = brand
      self.model = model
      self.year = year

   def __str__(self):
      return f"{self.year} {self.brand} {self.model}"

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2021)

# Print the object
print(my_car)  # Output: 2021 Toyota Corolla