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

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s : 
            return 0 
        s = s.strip()
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        res = 0 
        sign = 1 
        for i in range(len(s)):
            if s[i].isdigit():
                res = res * 10 + int(s[i])
            else : 
                if i == 0 and s[i] in ['+', '-']:
                    sign = 1 if s[i] == '+' else -1
                    continue
                else :
                    break
        res = sign * res     
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res
                
                
# hieu de bai la lam duoc +1: bo khoang trang , check ky tu dau tien, check chuoi so lien tuc sau do(neu bat dau = chu cai return luon 0 ) , check gioi han int32            
        


if __name__ == "__main__":
    # Tạo object 
    solution = Solution()
    print(solution.myAtoi("+0032abc"))
    
    
    