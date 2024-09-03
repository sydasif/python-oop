# Python Object-Oriented Programming


class Employee:
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = self.name + "." + last + "@abc.com"


emp_1 = Employee("John", "Doe", 50000)
emp_2 = Employee("Test", "User", 6000)

print(emp_1.email)
print(emp_2.email)
