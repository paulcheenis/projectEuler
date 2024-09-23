def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib = fibonacci(30)
len_fib = len(str(fibonacci(fib)))

print(fib)
print(len_fib)