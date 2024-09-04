class Employee:
    raise_amount = 1.04

    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = self.name + "." + last + "@abc.com"

    def full_name(self) -> str:
        return "{} {}".format(self.name, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("John", "Doe", 5000)
emp_2 = Employee("Test", "User", 6000)

emp_1.raise_amount = 1.05
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
