#anybase to Decimal by Sarvamm

#Checking a whether given number actually belongs to the base
#Crating a global variable l which will be used for calculations later
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

#Main Function --------------------------------
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
    
print(a2d("16AF2", 16)) #enter number and the base of the number