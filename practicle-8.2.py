class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating an object and initializing data
student1 = Student("Khush", 18)

# Displaying the data
student1.display()