def reverse(x):
    num = 0
    # negative = 0
    # if n < 0: 
    #     negative = 1
    #     n *= -1
    negative = -1 if x < 0 else 1
    while(x != 0):
        num = (num * 10) + x % 10
        x = x // 10 
    # if negative:
    #     num *= -1
    if (num < -2**31 or num > 2**31):
        return 0
    return num * negative       


print(reverse(123))
print(reverse(-321))
print(reverse(120))

