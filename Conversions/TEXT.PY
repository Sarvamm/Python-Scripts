# for i in range(10):
#     x = ord(str(i))
#     print(x , end=" ")
# print("\n") 

# for i in "ABCDEF":
#     x = ord(i)
#     print(x, end=" ")
#     print(i)
# print("\n")

# for i in "ABCDEF":
#     x = int(chr(ord(i) - 17)) + 10 
#     print(x, end=" ")
#     print(i, end=" ")

# # print("abc".upper())
# import random
# l=[]
# for i in range(11):
#     l.append(random.randint(0,24))
# print(l, end=" ")
# print(max(l))
for i in "ABCDEFGHIJ":
    print(i, int(chr(ord(i) - 17)) + 10)
for i in "KLMNOPQRST":
    print(i, int(chr(ord(i) - 27)) + 20)
for i in "UVWXYZ":
    print(i, int(chr(ord(i) - 37)) + 30)