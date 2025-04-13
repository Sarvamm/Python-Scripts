#Binary to Decimal (after checking whether user input really is binary)
def checkBin(bin=""):
    if(bin.count('0') + bin.count('1') == len(bin)):
        return True
    else:
        return False

def btod():
    x = input("Enter a binary number (only 0s and 1s)")
    hp = len(x)
    r = 0

    if checkBin(x):
        for i in x:
            r += int(i)*(2**hp)
            hp -= 1
        print("decimal conversion of ", x ," is ", r)
        cont = input("Do you wish to continue? (Y/N)")
        if cont == "Y" or "y":
            decision = True
        elif cont == "N" or "n":
            decision = False
        else:
            print("Invalid response, Program terminated")
            decision = False

        return(decision) 
    else:
        print("Invalid entry, Program terminated")
        return False
    
btod()