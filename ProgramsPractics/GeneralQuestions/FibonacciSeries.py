# Ex: 0 1 1 2 3 5 8 13 21
def fibonacci(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    a, b = 0, 1
    print(a, end=' ')
    for i in range(2, n+1):
        a, b = b, a + b
        print(a, end=' ')

fibonacci(10)