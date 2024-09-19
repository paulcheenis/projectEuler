def palindrome(check_number):
    num_to_string = str(check_number)
    reverse_string = num_to_string[::-1]
    half = int(len(num_to_string)/2)

    half_string_fwd = num_to_string[:half]
    half_string_fwd_check = half_string_fwd[::-1]
    half_string_rev = reverse_string[:half]
    half_string_rev_check = half_string_rev[::-1]

    if half_string_fwd_check == half_string_rev_check:
        return True
    else:
        return False

palindrome_products= []

for i in range (100, 1000):
    for j in range(100,1000):
        product = i * j
        if len(str(product)) % 2 == 0:
            if palindrome(product) == True:
                palindrome_products.append(product)

print(palindrome_products)
print(max(palindrome_products))

        