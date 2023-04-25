class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            y = max(stones) #Max
            stones.remove(y)
            x = max(stones) # 2nd Max
            if len(stones) + 1 != 2 and x == y: 
                stones.remove(x)
            elif x != y: 
                stones.append(y - x)
                stones.remove(x)
            elif(x == y and len(stones) == 1): 
                return y - x
        return stones[0]