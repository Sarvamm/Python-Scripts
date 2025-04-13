#! Binary to octal by Sarvamm
def checkBin(bin=""):
    bin = str(bin)
    if(bin.count('0') + bin.count('1') == len(bin)):
        return True
    else:
        return False

def b2d(x=""):
    x = str(x)
    hp = len(str(x)) - 1
    r = 0

    if checkBin(x):
        for i in str(x):
            r += int(i)*(2**hp)
            hp -= 1
    return r

def bintooct(bin=""):
    bin = str(bin)

    if len(bin)%3 == 1:
        bin = "00" + bin
    elif len(bin)%3 == 2:
        bin = "0" + bin

    l=[]
    x,y=0,3
    while y < len(bin) + 3:
        ele = bin[x:y]
        l.append(ele)
        x+=3
        y+=3
        ele=""
    r = ""

    for i in l:
        r += str(b2d(i))
    return(int(r))

print(bintooct(1000101010))

 