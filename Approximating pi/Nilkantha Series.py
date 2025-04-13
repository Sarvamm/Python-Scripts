#Approximating pi using Nilkantha Series
n = int(input("Enter precision (Higher is better, n = 100 will be accurate to 6 decimal places\n"))

pi = 3
k,j = 2, 0
for i in range(1,n+1):
    pi += 4*( (-1)**j/(k*(k+1)*(k+2)) )
    k += 2
    if j == 0:
        j = 1
    else:
        j = 0
print(pi)