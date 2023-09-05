class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self, fname, lname, number):
        super().__init__(fname, lname)
        self.studentNumber = number
        print('Student Created')  # Person Created

    # Override
    def who_am_i(self):
        print('I am a student')

    def say_hello(self):
        print('Hello')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

# Demonstration
def inheritance_example():
    p1 = Person('Lucas', 'Torreira')  # Person Created
    s1 = Student('Kerem', 'Akturkoglu', 7)  # Student Created
    t1 = Teacher('Dries', 'Mertens', 'Math')

    print(p1.firstname + ' ' + p1.lastname)
    print(s1.firstname + ' ' + s1.lastname + ' ' + str(s1.studentNumber))
    print(t1.firstname + ' ' + t1.lastname + ' ' + t1.branch)

    p1.who_am_i()
    s1.who_am_i()
    t1.who_am_i()

    p1.eat()
    s1.eat()
    s1.say_hello()

if __name__ == "__main__":
    inheritance_example()
