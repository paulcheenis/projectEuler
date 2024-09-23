def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(100))
str_fact = str(factorial(100))
total = 0

for i in str_fact:
    digit = int(i)
    total += digit

print(total)