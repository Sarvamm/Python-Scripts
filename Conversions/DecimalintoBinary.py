#decimal into binary
def dtob():
    deci = input("input decimal number")
    l=[]
    divi=int(deci)

    while divi != 0:
        l.append(divi%2)
        divi = divi//2
    r = ""
    for i in l[::-1]:
        r = r + str(i)

    print("Binary conversion of ", deci ," is ", r)
    cont = input("Do you wish to continue? (Y/N)")
    if cont == "Y" or "y":
        decision = True
    elif cont == "N" or "n":
        decision = False
    else:
        print("Invalid response, Program terminated")
        decision = False

    return(decision) 

dtob()