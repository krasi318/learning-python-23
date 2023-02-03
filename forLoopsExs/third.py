# Exercise 3: Calculate the sum of all numbers from 1 to a given number

a = 0
b = []
us_num = int(input("enter number "))
us_num = 10
for y in range(1, us_num + 1, 1):
    a += y
    b.append(y)
d = "+".join(str(x) for x in b)
print(a, d)