def convertToBase7(num):
    i = 0 
    result = 0
    while(num >= 7 ** i):
        i += 1
        if num <= 7 ** i:
            compare = (7 ** (i - 1))
            print(compare)
            result = result * 10
            print(result)
            result += (num // compare + 1)
            num -= (compare + 1) * (7 ** i - 1)
    return result

print(convertToBase7(-7))

