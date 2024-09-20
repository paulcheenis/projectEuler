import math

a = 3
b = 4
c = 5

abc_sum = a + b + c

while abc_sum != 1000:
    try:
        first_term = a**2 + b**2
        second_term = c**2
        abc_sum = a + b + c
    except ValueError:
        
        