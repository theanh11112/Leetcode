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
   def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        
        for i in range(len(val)):
            if num <= 0:
                break
            while num >= val[i]: 
                num -= val[i]
                roman_num += syms[i]
        return roman_num
    
         

                
    
            
                
        

  
    

if __name__ == "__main__":
    # Tạo object 
    solution = Solution()   
    # Test cases
    test_cases = [3, 4, 9, 58, 1994]
    for num in test_cases:                          
        result = solution.intToRoman(num)
        print(f"Input: {num} => Output: {result}")                   
    