def decitoany():
    deci = input("Enter a positive integer in decimal system: ")
    numsy = input("Enter number system to be converted into (e.g., 2 = binary, 8 = octal, 16 = hexadecimal).\nYou can pick any number between 2 and 36: ")

    if 0 < int(numsy) <= 36:
        l = []
        divi = int(deci)
        oppo = int(numsy)
        while divi != 0:
            l.append(divi % oppo)
            divi = divi // oppo
        r = ""
        for i in l[::-1]:
            if i >= 10:
                r += chr(i + 55)  # ASCII value of A=65, B=66 ...
            else:
                r += str(i)

        print(f"Conversion of {deci} to base {numsy} is: {r}")

        tryagain = input("try again? (Y/N)")
        if tryagain in "Yy":
            print(".\n.\n.\n")
            decitoany()

    else:
        print("Invalid number system. Please enter a base between 2 and 36.\n Let's Try Again\n .\n .\n .")
        decitoany()


decitoany()
