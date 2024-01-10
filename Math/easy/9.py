def isPalindrome(x): 
    num = 0
    y = x
    if x < 0: 
        return False
    while(x != 0):
        num = (num * 10) 
        num += x % 10
        x = x // 10 

    if y == num: 
        return True
    return False       

print(isPalindrome(121))