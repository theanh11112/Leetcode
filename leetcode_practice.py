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

   def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        else :
            s = str(x)
            center = len(s) // 2 
            a = center -1 
            b = center + 1 if len(s) % 2 == 1 else center 
            while a >= 0 and b < len(s) :
                if s[a] != s[b] :
                    return False 
                a -= 1 
                b += 1 
            return True
    # cach xai two pointers kha dai ( don gian hon thi chi can so sanh s voi s[::-1] chuoi dao nguoc la xong)

    # def isPalindrome(self, x):
    #    if x < 0 : 
    #       return False
    #    s = str(x)
    #    return s == s[::-1]
    

if __name__ == "__main__":
    # Tạo object 
    solution = Solution()
    print(solution.isPalindrome(121))  # True
    print(solution.isPalindrome(-121)) # False
    print(solution.isPalindrome(10))   # False
    
    
    