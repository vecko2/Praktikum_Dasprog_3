def f(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + f(n//2)
    else:
        return 1 + f(n-1)

n = int(input())
print(f"{(f(n))}")