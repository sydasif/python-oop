## Understanding Class Variables and Methods in Python

In our previous discussions, we explored the basics of creating classes and
methods in Python. Now, we'll move on to a crucial concept in Object-Oriented
Programming (OOP): class variables. These are variables shared among all
instances of a class, making them different from instance variables, which are
unique to each instance.

### What is a Class Variable?

A class variable is a variable that is shared by all instances of a class.
While instance variables like `name`, `last`, and `pay` are unique to each
instance of the `Employee` class, a class variable remains the same for all
instances unless explicitly modified. This characteristic makes class variables
ideal for data that should remain consistent across all instances.

### Example: Instance Variables vs. Class Variables

Let’s revisit our `Employee` class and see how instance and class variables
work together.

```python
class Employee:
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = self.name + "." + last + "@abc.com"

    def full_name(self) -> str:
        return "{} {}".format(self.name, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)  # Hardcoded raise amount
```

In this initial example, the `apply_raise` method uses a hardcoded value (1.04)
to increase the `pay` attribute by 4%. While this works, it’s not flexible.
What if we want to change the raise amount later or apply different raise
amounts to different instances? Hardcoding this value is not a good practice.

### Improving with Class Variables

To make our code more flexible, we can introduce a class variable,
`raise_amount`, that holds the raise percentage.

```python
class Employee:
    raise_amount = 1.04  # Class variable

    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = self.name + "." + last + "@abc.com"

    def full_name(self) -> str:
        return "{} {}".format(self.name, self.last)

    def apply_raise(self):
        # Using the class variable
        self.pay = int(self.pay * Employee.raise_amount)

```

### Explanation:

- **Class Variable**: `raise_amount` is now a class variable, meaning it is
  shared across all instances of the `Employee` class.
- **Instance Variables**: The `name`, `last`, `pay`, and `email` are still
  unique to each instance.

### Applying the Class Variable

Now, let's see how the `raise_amount` class variable affects the instances of
the `Employee` class.

```python
emp_1 = Employee("John", "Doe", 5000)
emp_2 = Employee("Test", "User", 6000)

print(emp_1.pay)  # Output: 5000
emp_1.apply_raise()
print(emp_1.pay)  # Output: 5200
```

#### Explanation:

- **Initial Pay**: `emp_1` starts with a salary of 5000.
- **Applying Raise**: The `apply_raise` method uses the `raise_amount` class
  variable (1.04) to increase the salary by 4%.
- **Updated Pay**: After applying the raise, the salary of `emp_1` becomes
    5200.

### Customizing Raise Amounts for Each Instance

What if we want to give a different raise to `emp_1` and `emp_2`? The current
setup doesn’t allow for this because the `apply_raise` method uses the class
variable `raise_amount`. To enable this customization, we can access the class
variable from the instance.

```python
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
        # Accessing the variable from the instance  
        self.pay = int(self.pay * self.raise_amount)  
```

With this setup, you can now customize the raise amount for each employee
instance.

```python
emp_1 = Employee("John", "Doe", 5000)
emp_2 = Employee("Test", "User", 6000)

emp_1.raise_amount = 1.05  # Custom raise for emp_1
print(emp_1.pay)  # Output: 5000
emp_1.apply_raise()
print(emp_1.pay)  # Output: 5250
```

#### Explanation:

- **Custom Raise**: We set `emp_1.raise_amount = 1.05`, which overrides the
  class variable for this particular instance.
- **Instance-Specific Raise**: Now, when `apply_raise` is called on `emp_1`,
  the custom raise amount (1.05) is used, resulting in a salary of 5250.

### Conclusion

Class variables provide a powerful way to manage data that should be consistent
across all instances of a class. By using class variables, you can avoid
hardcoding values and gain the flexibility to adjust behaviors across instances
easily. Additionally, by allowing instances to override class variables, you
can customize behavior at the instance level while maintaining a default for
all other instances. This balance of flexibility and consistency is a key
advantage of using class variables in Python OOP.