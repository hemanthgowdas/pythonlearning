from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 1:
            for i in range(len(strs) - 1):
                if  strs[i][:2] == strs[i+1][:2]:
                    for j in range(i+1):
                        if strs[i][:2] == strs[j][:2]:
                            return strs[i][:2]
            return ""
        else:
            return strs[0]

# Chat gpt solution
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""  
#         prefix = strs[0]  
#         for s in strs[1:]: 
#             while not s.startswith(prefix):  
#                 prefix = prefix[:-1]  
#                 if not prefix:
#                     return ""  
#         return prefix
        
    
sol = Solution()
result = sol.longestCommonPrefix(["ab", "a"])
print(result)