class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: 
            return n
        x = 1
        y = 1

        k = 0
        for i in range(n - 1):
            k = x + y  # x = num 1, y = num 2, add two together, temp
            x = y # update x to the next num y
            y = k # update y to the sum of the previous
        return k 
    
    def climbStairsAlt(self, n: int) -> int:
        if n < 3: 
            return n
        return self.climbStairsAlt(n - 1) + self.climbStairsAlt(n - 2)
