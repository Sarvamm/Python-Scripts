"""
Created by Sarvamm
THe program performs binomial expansion for expressions of the form (x + y)^n.
The user is prompted to input values for x, y (which can be integers or strings), and n (a natural number).
The program calculates the expansion using the binomial theorem, displaying each term in the expansion.
It provides different outputs based on the types of x and y, handling various cases, including integer and string inputs.
"""

def expand(x, y, n):
    x = str(x)  
    y = str(y)  
    print("(", x, "+", y, ")^", n, " =")
    for i in range(n+1):
        T = str(n) + "C" + str(i) + ". " + x + "^" + str(n - i) + ". " + y + "^" + str(i)
        if i < n:
            print(T, end=" + \n")
        else:
            print(T)    
        
def fct(n):
    r = 1
    while n > 0:
        r = r * n
        n -= 1
    return r

def C(n, r):
    if r <= n:
        return fct(n) / (fct(n-r) * fct(r))
    else:
        return "Error in r"

def bino(x, y, n):
    if isinstance(x, str) and isinstance(y, str):
        print("boing")
        for i in range(n+1):
            T = str(C(n, i)) + " . " + x + "^" + str(n-i) + " ." + y + "^" + str(i)
            if i < n:
                print(T, end=" + \n")
            else:
                print(T)
    elif isinstance(x, int) and isinstance(y, str):   
        for i in range(n+1):
            T = str(C(n, i) * (x**(n-i))) + " ." + y + "^" + str(i)
            if i < n:
                print(T, end=" + \n")
            else:
                print(T)
    elif isinstance(x, str) and isinstance(y, int):   
        for i in range(n+1):
            T = str(C(n, i) * (y**i)) + " ." + x + "^" + str(n-i)
            if i < n:
                print(T, end=" + \n")
            else:
                print(T)    
    elif isinstance(x, int) and isinstance(y, int):
        print((x + y) ** n)
    else:
        print("Error in input")  

def main():
    print("For a binomial in the form of: \n (x+y)^n,")
    x_input = input("Enter x, (int or char)\n")
    y_input = input("Enter y, (int or char)\n")
    try:
        x = int(x_input)
    except ValueError:
        x = x_input

    try:
        y = int(y_input)
    except ValueError:
        y = y_input

    n = int(input("Enter n, a natural number\n"))

    if n < 0:
        return("Invalid value of n")

    elif (isinstance(x, (int, str)) and isinstance(y, (int, str)) and isinstance(n, int)):
        expand(x, y, n)
        print("Which equates to ")
        bino(x, y, n)
        ch = input("Run again? (Y/N): ")
        if ch in "Yy":
            main()
        else:
            return    
    else:
        print("Input error")

main()