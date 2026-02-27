def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
a=int(input())
b=int(input())
x,y=a,b
while y:
    x,y=y,x%y
nsd=x
print(nsd)

def is_power_of_five(n):
    if n <= 0:
        return False
    while n % 5 == 0:
        n = n // 5

    return n ==1 
