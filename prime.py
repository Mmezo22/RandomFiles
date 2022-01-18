def prime_check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input())
print(prime_check(n))