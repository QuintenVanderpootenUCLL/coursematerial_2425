def is_prime(n):
    if n == 1 :
        return False
    for i in range(2, 9):
        print(n % i)
        if (n % i) == 0 and not(n == i):
            return False   
    return True
print(is_prime(1))
print(is_prime(9))
    