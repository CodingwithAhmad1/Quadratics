from sympy import *
import cmath 

x,y,z = symbols('x,y,z', real=True)

print("General form: ax**2 + bx +c = 0")

a = int(input("Enter a(a!=0): "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = (b**2 - 4*a*c)

sol_1 = (-b -cmath.sqrt(d))/ 2*a
sol_2 = (-b + cmath.sqrt(d))/ 2*a
sol_1 = str(sol_1)
sol_2 = str(sol_2)

expr = a*x**2 + b*x + c
print(expr.factor())

print(" ")
print("Rsults for equation: {a}x**2 + {b}x + {C} = 0")
if d>0:
    print("Type of roots: Two Distinct Real Roots")
elif d==0:
    print("Type of roots: Two Distinct Equal Real Roots")
elif d<0:
    print("Type of roots: Two Complex Roots")

sol_1 = sol_1.replace("0j", " ")
sol_2 = sol_2.replace("0j", " ")
sol_1 = sol_1.replace("+", " ")
sol_2 = sol_2.replace("+", " ")
sol_1 = sol_1.replace("(", " ")
sol_2 = sol_2.replace("(", " ")
sol_1 = sol_1.replace(")", " ")
sol_2 = sol_2.replace(")", " ")





print(f"The solutions are x = {sol_1}, and x = {sol_2}")
        
        