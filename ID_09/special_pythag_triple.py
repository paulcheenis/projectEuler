def pythagorean_triple(n):
    a = 2*n
    b = n**2 - 1
    c = n**2 + 1
    first_term = a**2 + b**2
    second_term = c**2
    sum = a + b + c
    product = a * b * c
    array = [first_term, second_term, sum, product]
    return array
        
# print(pythagorean_triple(21.8665))

def pythagorean_triple2(a, b, c):
    first_term = a**2 + b**2
    second_term = c**2
    sum = a + b + c
    product = a * b * c
    array = [first_term, second_term, sum, product]
    return array

#print(pythagorean_triple2(240,320,400)) #3, 4, 5
#print(pythagorean_triple2(150, 360, 390)) #5, 12, 13
#print(pythagorean_triple2(240, 320, 400)) #6, 8, 10
print(pythagorean_triple2(85, 455, 460))