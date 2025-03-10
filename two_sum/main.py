# Define a class called 'Dog'
class Dog:
    # Constructor method (__init__) initializes the object
    def __init__(self, name, age):
        self.name = name  # Attribute: name
        self.age = age    # Attribute: age

    # Method: A function that belongs to the class
    def bark(self):
        print(f"{self.name} says Woof!")

    # Method: A function that belongs to the class
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! Now you are {self.age} years old.")

# Create an object (instance of the Dog class)
dog1 = Dog("Buddy", 3)

# Access the object's attributes and methods
print(dog1.name)  # Access the attribute 'name' of the object
dog1.bark()       # Call the method 'bark' of the object
dog1.birthday()   # Call the method 'birthday' of the object

# Create another object (another instance of Dog)
dog2 = Dog("Bella", 5)

dog2.bark()       # Call the method 'bark' for another object
print(dog2.age)   # Access the 'age' attribute of dog2
