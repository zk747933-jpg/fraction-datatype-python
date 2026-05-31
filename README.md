# Fraction DataType Python

A custom Fraction data type implemented in Python using Object-Oriented Programming (OOP). This project demonstrates how to create a user-defined data type and perform arithmetic operations using operator overloading.

## Features

- Addition of fractions
- Subtraction of fractions
- Multiplication of fractions
- Division of fractions
- Operator Overloading
- Custom Data Type Implementation

## Concepts Used

- Classes and Objects
- Constructors (`__init__`)
- Magic Methods
- Operator Overloading
- OOP in Python
- Modules and Imports

## Project Structure

```text
fraction-datatype-python/
│
├── fraction.py
└── practice.py
```

## fraction.py

class Function:

    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)

    def __sub__(self, other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)

    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return "{}/{}".format(temp_num, temp_den)
        
## practice.py

```python
from fraction import Function

x = Function(11, 88)
y = Function(33, 11)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
```

## Sample Output

```text
3014/968
-2794/968
363/968
121/264
```

## Learning Outcomes

This project helped in understanding:

- User-defined data types
- Operator overloading
- Python magic methods
- Object-Oriented Programming (OOP)
- Working with modules and imports

## Author

Zishan Khan
