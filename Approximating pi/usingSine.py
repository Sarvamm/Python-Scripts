import math
n = int(input("enter a large number (5-7 digits)"))
# Convert degrees to radians
angle_degrees = 180
angle_radians = math.radians(angle_degrees)
from decimal import Decimal, getcontext

# Set precision to 3 decimal places
pi = Decimal((math.sin(angle_radians/99999))*99999)
print(pi)
# print(Decimal(math.pi))
# c=""
# r = Decimal(math.pi) - Decimal(pi)
# print(str(r), type(str(r)))
# for i in str(r)[-1:-5:-1]:
#     c = c + i
# c = c[::-1]
# c.lstrip("E")
# print(c)

# print("Accurate upto decimal places")