# Python Object-Oriented Programming
# Understanding Classes and Function in Python


class Employee:
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = self.name + "." + last + "@abc.com"

    def fullname(self):
        return "{} {}".format(self.name, self.last)


emp_1 = Employee("John", "Doe", 5000)
emp_2 = Employee("Test", "User", 6000)

print(Employee.fullname(emp_2))
