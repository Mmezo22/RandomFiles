def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_check(num):
    check = prime(num)

    if check == False:
        print(f"{num} is not a prime number.")
        return False
    else:
        print(f"{num} is a prime number.")
        return True

def prime_less(num):
    i = num - 1
    num_prime = 0
    while i>1:
        if prime(i) == True:
            num_prime += 1
        i -= 1
    print(f'There are {num_prime} prime numbers less than {num}.')

n = int(input())
prime_check(n)
prime_less(n)