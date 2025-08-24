def factorial(n):
    if n<2:
        return 1
    return n * (factorial(n-1))

k=int(input("Enter a number: "))
result=factorial(k)
print(f"Factorial of {k} is: {result}")
