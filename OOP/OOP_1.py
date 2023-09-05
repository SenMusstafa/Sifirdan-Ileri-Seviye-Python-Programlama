class Person:
    # Class attribute
    address = 'no information'
    
    # Constructor (init method)
    def __init__(self, name, year):
        # Object attributes
        self.name = name
        self.year = year
        
    # Instance methods
    def intro(self):
        print('Hello there, I am ' + self.name)
    
    def calculate_age(self):
        return 2023 - self.year

# Object (instance) creation
def class_example():
    p1 = Person(name='Mauro', year=1993)
    p2 = Person(name='Fernando', year=1987)

    p1.intro()
    p2.intro()

    print(f'My name is {p1.name} and I am {p1.calculate_age()} years old.')
    print(f'My name is {p2.name} and I am {p2.calculate_age()} years old.')

if __name__ == "__main__":
    class_example()
