## Understanding Classes and Methods in Python

In this blog, we’ll build upon our previous discussion on classes in Python by
exploring how to define and use methods within a class. We'll continue with the
example we used earlier.

```python
class Employee:
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = self.name + "." + last + "@abc.com"


emp_1 = Employee("John", "Doe", 5000)
emp_2 = Employee("Test", "User", 6000)
```

### Understanding Methods in Python Classes

Methods in Python are similar to functions but are associated with a class.
They describe actions or behaviors that the instances (objects) of the class
can perform. These methods can interact with the data stored in an instance,
allowing us to manage and manipulate that data effectively.

### Instance Methods

The primary focus of this post is on instance methods. These are the most
common methods used in classes. An instance method automatically receives the
instance as its first argument, traditionally named `self`. This allows the
method to access and modify the instance's data.

#### Example: Creating an Instance Method

Let's say we want to retrieve the full name of an employee. We could do this
manually:

```python
class Employee:
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = self.name + "." + last + "@abc.com"


emp_1 = Employee("John", "Doe", 5000)
emp_2 = Employee("Test", "User", 6000)

print("{} {}".format(emp_1.name, emp_1.last))  # Output: John Doe
```

While this works, it’s not an efficient way to handle this for every employee.
Instead, we can define an instance method within the class to automate this
process:

```python
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

print(emp_1.fullname())
print(emp_2.fullname())
```

Now, when we call the `fullname()` method on each instance, it prints the full
name for each employee:

```shell
John Doe
Test User
```

### Common Pitfall: Forgetting the `self` Argument

A common mistake when defining instance methods is forgetting to include
the `self` argument. This argument is essential because it links the method to
the instance. If you omit `self`, you’ll run into an error. Consider this
example:

```python
class Employee:
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = self.name + "." + last + "@abc.com"

    def fullname():
        return "{} {}".format(self.name, self.last)


emp_1 = Employee("John", "Doe", 5000)
emp_2 = Employee("Test", "User", 6000)

print(emp_1.fullname())
```

Running this code will result in the following error:

```shell
Traceback (most recent call last):
  File "C:\PycharmProjects\python-oop\corey\02_OOP.py", line 20, in <module>
    print(emp_1.fullname())
          ^^^^^^^^^^^^^^^^
TypeError: Employee.fullname() takes 0 positional arguments but 1 was given
```

This error occurs because Python automatically passes the instance (`emp_1` in
this case) as the first argument to the `fullname()` method. Since we didn’t
include `self`, Python doesn’t know where to assign the instance, leading to
a `TypeError`.

### Calling an Instance Method from the Class

Another important point to note is that you can also call an instance method
directly from the class itself by passing the instance as an argument:

```python
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

print(Employee.fullname(emp_1))
```

In this example, instead of calling `emp_1.fullname()`, we
use `Employee.fullname(emp_1)`. This approach works because we explicitly
pass `emp_1` as the instance to the `fullname()` method. This flexibility shows
how Python allows you to interact with methods in multiple ways, providing both
convenience and control.

### Conclusion

In this post, we explored how to define and use methods within a Python class,
focusing on instance methods. These methods play a crucial role in defining the
actions that instances can perform, and they allow you to work efficiently with
the data stored in those instances.

We also highlighted common pitfalls, such as forgetting the `self` argument,
and demonstrated how you can call instance methods directly from the class.
Understanding these basics will help you create more powerful and flexible
Python programs.