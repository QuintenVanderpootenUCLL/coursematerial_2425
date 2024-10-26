def gcd(x, y):
    start = min(abs(x), abs(y))
    for i in range(start, 0, -1):
        if (x % i) == 0 and (y % i) == 0:
            return i
    return 1

print(gcd(10, -15))
print(gcd(15, 10))
print(gcd(5, 7))