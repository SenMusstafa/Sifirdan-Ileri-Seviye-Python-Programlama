class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    # Method to calculate circumference
    def calculate_circumference(self):
        return 2 * self.pi * self.radius
    
    # Method to calculate area
    def calculate_area(self):
        return self.pi * (self.radius ** 2)

# Circle object creation
def circle_example():
    c1 = Circle()  # Default radius is 1
    c2 = Circle(5)

    print(f'c1: Area = {c1.calculate_area()}, Circumference = {c1.calculate_circumference()}')
    print(f'c2: Area = {c2.calculate_area()}, Circumference = {c2.calculate_circumference()}')

if __name__ == "__main__":
    circle_example()
