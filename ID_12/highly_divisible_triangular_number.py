def triangle(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def factor_array(n):
    array = []
    for i in range(1, n+1):
        if n % i == 0:
            array.append(i)
    return array

print(triangle(7)) # expect 28
print(factor_array(triangle(7)))
print(len(factor_array(triangle(7))))

print(triangle(75000)) 
#print(factor_array(triangle(50000)))
print(len(factor_array(triangle(75000))))