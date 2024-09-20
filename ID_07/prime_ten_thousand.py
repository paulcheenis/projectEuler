prime_numbers = [2, 3, 5, 7, 11, 13]
count = 6
number = 13

while count <= 15:
    number += 1
    for i in range(2, number):
        #print(number)
        if (number % i == 0):
            #print("This number ain't prime!")
            number += 1
            break
        prime_numbers.append(number)
        count += 1


print(prime_numbers)
