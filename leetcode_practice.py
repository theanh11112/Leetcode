# leetcode_practice.py

"""
LeetCode Practice File
----------------------
Hướng dẫn:
1. Viết code trong class Solution theo yêu cầu của bài LeetCode.
2. Thêm test case trong phần main để chạy thử.
3. Chạy file bằng lệnh: python leetcode_practice.py
"""

from typing import List
import numpy as np


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs :
           return ''
        
        shortest = min(strs, key=len)
        result = ''
        for i in range(len(shortest)) :
            for j in range(len(strs)) :
                if (shortest[i] != strs[j][i]):
                   return result
            result += strs[0][i]
            
        return result
        
    
                
        

  
    

if __name__ == "__main__":
    # Tạo object 
    solution = Solution()   
    # Test case 1  
    print(solution.longestCommonPrefix(["flower","flow","flight"]))  # 👉 "fl"
    print(solution.longestCommonPrefix(["dog","racecar","car"]))     # 👉 ""
    print(solution.longestCommonPrefix(["interspecies","interstellar","interstate"]))  # 👉 "inters"
 
