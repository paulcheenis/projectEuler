n = 13
collatz = 1
max_collatz = 0
max_n = 0

for i in range(2, 1000000):
    collatz = 1
    while n != 1:
        if (n % 2 == 0):
            n = n/2
            collatz += 1
        elif (n % 2 != 0):
            n = 3*n + 1
            collatz += 1
    if collatz > max_collatz:
        max_collatz = collatz
        max_n = i


print(max_collatz) # expect 10
print(max_n)
