## Understanding Classes, Attributes, and Instances in Python

In this blog series, we’re going to break down the essentials of
Object-Oriented Programming (OOP) in Python. While OOP is a vast topic, this
series will focus on the foundational elements. By dividing the content into
multiple posts, we can concentrate on specific areas, making it easier to grasp
the concepts.

### Why Use Classes?

Classes in Python serve as a way to organize and manage your code. They allow
you to group related data and functions together, making your code more modular
and reusable.

### What are Attributes?

Before we dive deeper, it’s important to understand what an attribute is. In
Python, attributes (also known as variables or properties of a class) are
pieces of data associated with instances of a class. These attributes hold
values that define the state or characteristics of an object.

For example, in a class representing an employee, attributes could include the
employee's name, surname, and salary. Each instance of the class can have
different values for these attributes, making them unique.

### Creating a Class

To define a class in Python, use the `class` keyword. Let's start with a simple
example:

```python
class Employee:
    pass
```

This is a basic `Employee` class with no attributes or methods. Even though
it’s empty, we can still create objects (instances) from it:

```python
class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

```

Running this code will output something like:

```
<__main__.Employee object at 0x000002239B1D3A40>
<__main__.Employee object at 0x000002239B1D1580>
```

This shows that `emp_1` and `emp_2` are unique objects, each occupying a
different memory space.

### Adding Attributes to Instances

To make our class more meaningful, we can manually add attributes to the
instances:

```python
class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()

emp_1.name = "John"
emp_1.last = "Doe"

emp_2.name = "Test"
emp_2.last = "User"

```

These attributes — `name` and `last` — are now associated with `emp_1` and
`emp_2`. If you print them, we get the name:

```shell
John
Test
```

Each instance has its own set of attributes, making them distinct from one
another. However, adding attributes manually isn’t ideal because it leads to
repetitive code and increases the risk of errors.

### Attribute Assignment with the `__init__` Method

Python provides a built-in method called `__init__()` to streamline the process
of setting up instance attributes. This method is automatically invoked when a
new object is created.

```python
class Employee:
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = self.name + "." + last + "@abc.com"
```

Here’s what happens in the code above:

- `__init__()` is a special method used to initialize the object’s attributes.
- The `self` keyword refers to the current instance of the class.
- Attributes like `name`, `last`, and `pay` are set up when a new `Employee`
  object is created.
- The `email` attribute is automatically generated based on the `name`
  and `last` attributes.

### Example of Using the `__init__` Method

Let's see this in action:

```python
class Employee:
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = self.name + "." + last + "@abc.com"


emp_1 = Employee("John", "Doe", 5000)
emp_2 = Employee("Test", "User", 6000)

print(emp_1.email)
print(emp_2.email)
```

In this example, when `Employee` objects are created, the `__init__` method
automatically sets up their attributes. The keyword `self` ensures that each
object maintains its own set of attributes.

Running this code will give us:

```shell
John.Doe@abc.com
Test.User@abc.com
```

### Conclusion

In this post, we explored the basics of creating classes and instances in
Python, focusing on attributes. We defined what attributes are and how they
relate to the objects created from a class.

We also covered how to automate the assignment of attributes using the
`__init__` method. Understanding these basics is crucial as we move forward
into more complex OOP concepts. Stay tuned for the next post, where we’ll
continue building on these fundamentals!
