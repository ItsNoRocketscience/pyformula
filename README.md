# pyformula

This python package defines a class for easy access to a formula solved for all its variables.
It uses sympys symbols, expressions and solve method for handling symbolic expressions.

Basic example

```Python
x, y = sympy.symbols('x y')
formula = pyformula.Formula(2*x + y)

print(formula.y(x=2))  # should print -4
print(formula.x(y=-2)) # should print 1
```
