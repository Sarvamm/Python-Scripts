#Octal to Decimal (after checking whether user input really is Octal)
def checkOct(bin=""):
    if("89" in bin):
        return False
    else:
        return True

def otod():
    x = input("Enter a Octal number")
    hp = len(x)-1
    r = 0

    if checkOct(x):
        for i in x:
            r += int(i)*(8**hp)
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
    
otod()