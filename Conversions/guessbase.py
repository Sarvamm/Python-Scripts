#by Sarvamm
# The function checks if the number belongs 
# to the specified base system.
# For example, "117A" is invalid in base < 11
# but valid in bases 11 or higher.
# Returns false for base < 11, 
# and true otherwise.

def checkbase(x , base):
    x = str(x)
    base = int(base)
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
        return False
    
print(checkbase("ggez", 20))

