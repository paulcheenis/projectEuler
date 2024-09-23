
power_digit = 2 ** 1000
print(power_digit)

str_power_digit = str(power_digit)
total = 0
for i in str_power_digit:
    digit = int(i)
    total += digit

print(total)