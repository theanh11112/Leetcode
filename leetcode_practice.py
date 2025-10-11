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

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        Int_Max = 2**31 -1 
        Int_min = -2**31 
        sign = 1 if x >= 0 else -1 
        x = abs(x)

        if x == 0 : 
            return 0 
        else :
            res = 0 
            while x > 0 :
                digit = x % 10 
                res = res * 10 + digit
                if res < Int_min or res > Int_Max :
                   return 0
                x = x // 10 
            return sign * res 
            

# lesson 7 leetcode : Reserve Interger : solution  =>  chia lay nguyen va chia lay du cho 10 
# tim hieu toi uu bai toan thi sau moi lan them duoc so moi vao trong vao so hien tai thi len check xem da overflow chua 
    

    


if __name__ == "__main__":
    # Tạo object 
    solution = Solution()
    print(solution.reverse(-123))
    
    