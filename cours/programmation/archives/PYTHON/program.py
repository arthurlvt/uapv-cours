class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle1 = rectangle(5, 10)
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())