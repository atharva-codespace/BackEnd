class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"This is a shape called '{self.name}'."

    def area(self):
        return 0


class Circle(Shape):

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def run_demo():
    circle = Circle(radius=7)
    rectangle = Rectangle(length=10, breadth=5)
    triangle = Triangle(base=8, height=6)

    print("Output:")
    for shape in (circle, rectangle, triangle):
        print(shape.describe())           
        print(f"Area of {shape.name} = {shape.area():.2f}")  
        print("-" * 30)
