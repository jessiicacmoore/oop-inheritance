class Person:
    """A class that represents a person"""

    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"Hi, my name is {self.name}"


class Student(Person):
    """A class that represents a student"""

    def learn(self):
        return "I get it!"


class Instructor(Person):
    """A class that represents an instructor"""

    def teach(self):
        return "An object is an instance of a class"


nadia = Instructor("Nadia")
print(nadia.greeting())


chris = Student("Chris")
print(chris.greeting())


print(nadia.teach())
print(chris.learn())
print(chris.teach())  # teach will not work on Chris because he is from the child class Student, not Teacher and the teach function doesn't exist in the parent class of Person or in the Student class
