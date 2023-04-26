class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while num: # while num is not 1
            sum += num % 10 # get the last digit of num
            num //= 10 # removes the last digit
        if sum < 10: #check if num is less than 10 and return sum
            return sum
        return self.addDigits(sum) # if not, recursively call the function to get desired output