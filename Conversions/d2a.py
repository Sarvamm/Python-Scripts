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
print(d2a(16,2))
