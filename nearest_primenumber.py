def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True


def nearest_prime(n):
    if n <= 2:
        return 2

    d = 0
    while True:
        if is_prime(n - d):
            return n - d
        if is_prime(n + d):
            return n + d
        d += 1
print(nearest_prime(10))