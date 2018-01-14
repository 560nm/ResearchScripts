from sympy import *

x = symbols('x')
tosolve = input("Enter the equation, for example, -0.0201*2+46.964*x+563.96:")
howmany = int(input("How many samples: "))

for a in range(0, howmany):
    read = int(input("Enter fluorescent read value:"))
    x, y = symbols('x y')
    y = solve(Eq(tosolve, read), x)
    print(y) #error
