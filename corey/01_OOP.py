# Understanding Classes, Attributes, and Instances in Python


# Define a class named Employee
class Employee:
    # The __init__ method is a special method called when an object is
    # created. It initializes the attributes of the class with values
    # provided during the creation of an object.
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = self.name + "." + last + "@abc.com"


# Create instances (objects) of the Employee class with different attributes
emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Test", "User", 6000)

# Print the email address for each employee instance
print(emp_1.email)
print(emp_2.email)
