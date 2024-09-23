def get_primes(max):
    prime_numbers = []
    for i in range(2, max):
        prime_flag = 0
        for j in range(2, i):
            if i % j == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            prime_numbers.append(i)
    return prime_numbers

def sum_primes(array):
    total = 0
    for i in array:
        total += i
    return total

print(sum_primes(get_primes(2000000)))