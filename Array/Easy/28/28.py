class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      for i in range(len(haystack)): 
        if needle[0] == haystack[i]:
           for j in range(len(needle)): 
              if needle == haystack[i: i + len(needle)]: 
                 return i
              else: 
                break
      return -1 

set1 = Solution().strStr("sadbutsad", "sad")
print(set1)