# Prime factors of 13195 are 5, 7, 13, and 29.

factors = []
prime_factors = []

def prime_factor_branch(number):
    for i in range(2, (number //2) + 1):
        if number % i == 0:
            factors.append(i)
            branch = int(number / i)
            # print(i)
            return branch
    
#fugazi recursion
print(prime_factor_branch(600851475143))
print(prime_factor_branch(prime_factor_branch(600851475143)))
print(prime_factor_branch(prime_factor_branch(prime_factor_branch(600851475143))))
print(prime_factor_branch(prime_factor_branch(prime_factor_branch(prime_factor_branch(600851475143)))))
#print(factors)