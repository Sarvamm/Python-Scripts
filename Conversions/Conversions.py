# Decimal to Binary Conversion
def dtob():
    deci = input("Input decimal number: ")
    l = []
    divi = int(deci)

    while divi != 0:
        l.append(divi % 2)
        divi = divi // 2
    r = ""
    for i in l[::-1]:
        r += str(i)

    print("Binary conversion of", deci, "is", r)
    
    cont = input("Do you wish to continue? (Y/N): ")
    if cont == "Y" or cont == "y":
        return True
    elif cont == "N" or cont == "n":
        return False
    else:
        print("Invalid response, Program terminated.")
        return False


# Binary to Decimal Conversion (after checking binary input)
def checkBin(bin=""):
    return bin.count('0') + bin.count('1') == len(bin)

def btod():
    x = input("Enter a binary number (only 0s and 1s): ")
    hp = len(x) - 1
    r = 0

    if checkBin(x):
        for i in x:
            r += int(i) * (2 ** hp)
            hp -= 1
        print("Decimal conversion of", x, "is", r)
        
        cont = input("Do you wish to continue? (Y/N): ")
        if cont == "Y" or cont == "y":
            return True
        elif cont == "N" or cont == "n":
            return False
        else:
            print("Invalid response, Program terminated.")
            return False
    else:
        print("Invalid entry, Program terminated.")
        return False


# Main Program Loop
run = True
while run:
    opchoice = input("What operation do you want to perform? (A,B) --> (DecimalToBinary, BinaryToDecimal): ")
    
    if opchoice in "Aa": 
        run = dtob()

    elif opchoice in "Bb":
        run = btod()
    
    else:
        print("Invalid Input, Program terminated.")
        run = False
