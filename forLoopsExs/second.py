# Exercise 2: Print the following pattern
row = 6
for i in range(1, row + 1, 1):

    for j in range(1, i - i):
        print(j, end=' ')

    print("")