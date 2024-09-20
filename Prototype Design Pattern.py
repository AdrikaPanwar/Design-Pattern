# PROBLEM

import copy

class Shape:
    def clone(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def clone(self):
        # deepcopy() to create copies of object
        return copy.deepcopy(self)

    def __str__(self):
        return f"Circle with radius: {self.radius}"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def clone(self):
        
        return copy.deepcopy(self)

    def __str__(self):
        return f"Square with side: {self.side}"


def client_code(shape: Shape):
    shape_clone = shape.clone()
    print(f"Original: {shape}")
    print(f"Cloned: {shape_clone}")


circle = Circle(10)
client_code(circle)

square = Square(20)
client_code(square)
