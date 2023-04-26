class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        negative = 0
        if x < 0: # checking for negative
            negative = 1
            x *= -1
        while(x != 0):
            num *= 10 # add a place holder to add the next value
            num += x % 10 # gets the last digit
            x = x // 10 # removes the last digit
        if negative:
            num *= -1
        if num < -2**31 or num > 2**31 - 1:
            return 0
        return num
