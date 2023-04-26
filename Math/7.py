class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        n = x
        negative = 0
        if n < 0: 
            negative = 1
            n *= -1
        while(n != 0):
            num *= 10 
            num += n % 10
            n = n // 10 # Get the number before the decimal and round it up
        if negative:
            num *= -1
        if num < -2**31 or num > 2**31 - 1:
            return 0
        return num
