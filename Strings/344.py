def reverseString(s): 
    length = len(s)
    for i in range(len(s) // 2): 
        temp = s[i]
        s[i],  s[length - i - 1] = s[length - i - 1], temp
    return s

print(reverseString(["h","e","l","l","o"]))