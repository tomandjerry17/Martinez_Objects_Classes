class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area_formula = 3.1416 * self.radius**2
        print(f"Area is >>{area_formula:.2f}<< if the radius is equal to ({self.radius})")

    def perimeter(self):
        perimeter_formula = 2 * 3.1416 * self.radius
        print(f"Perimeter is >>{perimeter_formula:.2f}<< if the radius is equal to ({self.radius})")


r = int(input("Enter an integer: "))
print()
result = Circle(r)

result.area()
result.perimeter()
