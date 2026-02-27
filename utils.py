def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
def nsd(a,b):
    a=abs(a)
    b=abs(b)
    while b!=0:
        a,b=b,a%b
    return a
def fibonacci(n):
    """Повертає n-те число Фібоначчі"""
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


def is_power_of_five(n):
    if n <= 0:
        return False
    while n % 5 == 0:
        n = n // 5

    return n ==1 
