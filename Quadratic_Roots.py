import math

a = int(input("coefficient of x^2:\n"))
b = int(input("coefficient of x:\n"))
c = int(input("constant term:\n"))

def findRoots(a = 1, b = 1, c = 1):
    if a == 0:
        print("coeffecient of x^2 must be non zero")
        return
    discriminant = (b**2) - (4*a*c)
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a) 
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(root1, root2)

    elif discriminant == 0:
        root = -b / (2*a)
        print("Root is", root)
    else:
        print("No real roots")
        return 
findRoots(a,b,c)
