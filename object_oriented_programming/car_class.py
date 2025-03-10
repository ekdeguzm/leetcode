# Define a class called 'Car'
class Car:
    # Constructor method (__init__) initializes the object
    def __init__(self, make, model, year):
        self.make = make  # Attribute: name
        self.model = model    # Attribute: age
        self.year = year  

    # Method: A function that belongs to the class
    def start(self):
        print(f"The {self.year} {self.make} {self.model} car is starting!")

    # Method: A function that belongs to the class
    def stop(self):
        print(f"The {self.year} {self.make} {self.model} car is stopping!")

# Create an object (instance of the Car class)
car1 = Car("Toyota", "CR-V", 2020)

# Access the object's attributes and methods
print(car1.make)  # Access the attribute 'make' of the object
car1.start()       # Call the method 'start' of the object
car1.stop()   # Call the method 'stop' of the object

# Create another object (another instance of Car)
car2 = Car("Subaru", "Crosstrek", 2005)

car2.start()       # Call the method 'start' for another object
print(car2.year)   # Access the 'year' attribute of car2
