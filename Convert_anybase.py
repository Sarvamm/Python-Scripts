#A project by Sarvamm
#A program that can convert any number of any base into another base.
#constraints: 36 >= base >= 2


#Checking whether given number actually belongs to the base
#Creating a global variable l which will be used for calculations later
def checkbase(x , base):
    x = str(x)
    base = int(base)
    global l
    l=[]
    for i in x:
        if i.lower() in "abcdefghij":
            i = i.upper()
            l.append(int(chr(ord(i) - 17)) + 10)
 

        elif i.lower() in "klmnopqrst":
            i = i.upper()
            l.append(int(chr(ord(i) - 27)) + 20)
    

        elif i.lower() in "uvwxyz":
            i = i.upper()
            l.append(int(chr(ord(i) - 37)) + 30)

        else:
            l.append(i)
    for i in l:
        if type(i) != int:
            l[l.index(i)] = int(i)

    if max(l) < base:
        return True
    else:
        print("Invalid input, please check base and try again")
        return False
 
 #Checking validity of given input
def isValid(x,base):
    for char in x:
        if not (char.isdigit() or char.lower() in 'abcdefghijklmnopqrstuvwxyz'):
            print("Invalid entry, only alphanumeric allowed")
            return False
        elif base > 36 or base < 2:
            print("Invalid base (2-36 allowed)")
            return False
    return True

#Any number into Decimal --------------------------------
def a2d(x, base):
    x = str(x)
    base = int(base)  

    if isValid(x,base):
        if checkbase(x, base):
            global l
            r=0
            hp = len(l) - 1
            for i in l:
                r += int(i)*(base**hp)
                hp -= 1
            return r
#Decimal number into given base --------------------------------
def d2a(x, base):

    if 0 < int(base) <= 36:
        l = []
        divi = int(x)
        oppo = int(base)
        while divi != 0:
            l.append(divi % oppo)
            divi = divi // oppo
        r = ""
        for i in l[::-1]:
            if i >= 10:
                r += chr(i + 55)  # ASCII value of A=65, B=66 ...
            else:
                r += str(i)
        return r
    else:
        print("invalid base")
        return

#main function --------------------------------
def main(x, base1, base2):
    inDecimal = a2d(x, base1)
    inBase = d2a(inDecimal, base2)
    print(f"The number {x} is equivalent to {inBase} in base {base2}.")
    return inBase

#Testing the program
main("16aF2", 16, 36) #Number give, Base of number, Base to be converted to.