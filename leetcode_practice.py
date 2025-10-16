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
   def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0 
        i = 0 
        while i < len(s):
            if i + 1 < len(s) and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                total += roman_numerals[s[i + 1]] - roman_numerals[s[i]]
                i += 2
            else:
                total += roman_numerals[s[i]]
                i += 1  
        return total
            
                
        

  
    

if __name__ == "__main__":
    # Tạo object 
    solution = Solution()   
    # Test case 1   
    s = "MCMXCIV"
    result = solution.romanToInt(s)
    print(f"Input: s = {s}")
    print(f"Output: {result}")  # Expected output: 1994