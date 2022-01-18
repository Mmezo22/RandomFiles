def fib(num):
    first = 1
    second = 1
    if num <= 0:
        return []
    elif num == 1:
        return [first]
    elif num == 2:
        return [first, second]
    elif num >= 2:
        result = [first, second]
        for i in range(num-2):
            add = first + second
            result.append(add)
            first = second
            second = add
        return result

n = int(input("How many Fibonnaci numbers: "))
print(fib(n))