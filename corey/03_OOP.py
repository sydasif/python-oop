class Employee:
    # Class variable shared among all instances
    raise_amount = 1.04

    def __init__(self, name, last, pay):
        # Instance variables unique to each instance
        self.name = name
        self.last = last
        self.pay = pay
        self.email = self.name + "." + last + "@abc.com"

    def full_name(self) -> str:
        # Method to return the full name of the employee
        return "{} {}".format(self.name, self.last)

    def apply_raise(self):
        # Method to apply the raise to the employee's salary
        self.pay = int(self.pay * self.raise_amount)


# Creating instances of the Employee class
emp_1 = Employee("John", "Doe", 5000)
emp_2 = Employee("Test", "User", 6000)

# Overriding the raise_amount for emp_1 only
emp_1.raise_amount = 1.05

# Printing the original salary of emp_1
print(emp_1.pay)  # Output: 5000

# Applying the raise to emp_1's salary
emp_1.apply_raise()

# Printing the updated salary after applying the raise
print(emp_1.pay)  # Output: 5250 (5000 * 1.05)
