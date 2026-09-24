class Student:
    name = "Khush"
    age = 18

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating an object
student1 = Student()

# Accessing class attributes
print("Name:", student1.name)
print("Age:", student1.age)

# Accessing class method
student1.display()