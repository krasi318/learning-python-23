# Exercise 4: Write a program to print multiplication table of a given number
a = 1
li = []
us1_num = int(input("enter num "))
li.append(us1_num)
for f in range(1, 10, 1):
    a += 1
    li.append(a * us1_num)

for j in li:
    print(j)

