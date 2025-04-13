#Hexadecimal to Decimal by Sarvamm
def isHexadecimal(s):
    for char in s:
        if not (char.isdigit() or char.lower() in 'abcdef'):
            return False
    return True
def h2d(x=""):
    x = str(x)  
    if isHexadecimal(x):
        l = []
        for i in x:
            if i in "abcdef":
                l.append(i.upper())
            else:
                l.append(i)
        for i in l:
            if i in "ABCDEF":
                l[l.index(i)] = str(int(chr(ord(i) - 17)) + 10) 

        r=0
        hp = len(l) - 1
        for i in l:
            r += int(i)*(16**hp)
            hp -= 1
        return r
print(h2d("16af2"))