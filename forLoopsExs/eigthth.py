# Exercise 8: Print list in reverse order using a loop
# Given:
#
# list1 = [10, 20, 30, 40, 50]
# Expected output:
#
# 50
# 40
# 30
# 20
# 10

list1 = [10, 20, 30, 40, 50]
a = 0
b = 0
list2 = []
for i in list1:
    a = list1[b]
    b += 1
    list2.insert(0, a)
    print(a)

print(list2)
