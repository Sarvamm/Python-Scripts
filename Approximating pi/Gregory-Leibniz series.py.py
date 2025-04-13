#Approximating pi using Gregory-Leibniz series 

n = int(input("Enter precision. (Higher is better but slower, less than 100 is inaccurate)\n"))
pi = 0


k, j = 1, 0
for i in range(1 ,n+1):
    pi += (4/k)*float((-1)**(j))
    k += 2
    if j == 0:
        j = 1
    else: 
        j = 0

print(pi)
