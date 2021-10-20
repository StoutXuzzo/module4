def factorial(num):
    res = num
    while num != 1:
        res = res * (num - 1)
        num -= 1
    return res

def recursiveFactorial(num):
    if num == 1:
        return 1
    num = num * recursiveFactorial(num-1)
    return num

print(factorial(5))
print(recursiveFactorial(5))