from itertools import product
import random 
nums = [1,2,3,4,5,6,7,8,9]
ops = ["*", "/", "+", "-"]

def gencomb(k):
    return list(product(range(10), repeat=k))

# Example usage

def genq1():
    global nums, ops
    Q = ''
    expression = str(random.choice(nums))
    for _ in range(random.randint(2, 4)):
        expression += ' ' + random.choice(ops) + ' ' + str(random.choice(nums))
    result = eval(expression)
    if type(result) == int:
        
        for i in expression:
            if i.isdigit():
                Q += random.choice(['_',i])
            else:
                Q += i
        print(Q, '= ', result)
        return Q, result
    else:
        return genq1()
def uinput():
    t = genq1()
    Q, result = t[0], t[1]
    Qla = Q.split()
    for i in range(Qla.count('_')):
        a=str(int(input("enter")))
        Qla[Qla.index('_')] = a
        Q=''
        for i in Qla:
            Q+=i+' '
        print(Q, '= ', result)
    return (Q, result, Qla)

Q, result , Qla = uinput()
def won():
    
    global Q, result, Qla
    if eval(Q) == result:
        print('Won')
        return True
    else:
        print('Lost')
        return False
won()