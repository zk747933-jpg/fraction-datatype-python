from fraction import Fraction

x = Fraction(11,88)
y = Fraction(33,11)

print(x.__add__(y))
print(x.__mul__(y))
print(x.__truediv__(y))
print(x.__sub__(y))
print(x.__str__())
print(y.__str__())