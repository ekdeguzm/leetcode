# Define a class called 'Car'

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


# Create an object (instance of the Car class)
rectangle1 = Rectangle(5,3)

# Access the object's attributes and methods
print("Area:", rectangle1.area()) 
print("Perimeter:", rectangle1.perimeter())  
print("Width:", rectangle1.width)
print("Height:", rectangle1.height)

# Create another object (another instance of Car)
rectangle2 = Rectangle(2, 1)
print("Area of second rectangle:", rectangle2.area())
print("Perimeter of second rectangle:", rectangle2.perimeter())
