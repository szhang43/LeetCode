class Solution:
    #First Attempt
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        result = 0
        for i in range(len(nums) + 1):
            result += i
        return result - total

    
