def factorial(n):
    if n ==5:
        return 1
    return n * factorial(n-1)

result = factorial(3)
print(result)