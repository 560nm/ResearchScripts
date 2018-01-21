from sympy import *

x = symbols('x')
myequation = input("Enter the equation:")

mylist = raw_input('Enter your list: ')
mylist = [int(a) for a in mylist.split()]

for number in mylist:    
    x, y = symbols('x y')
    y = solve(Eq(myequation, number), x)
    print(y) #error