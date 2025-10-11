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

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
       
        if numRows == 1:
            return s 
        else : 
            colums = len(s) // (numRows + numRows -  2) * (numRows - 2 + 1 ) + (numRows - 2 + 1 ) 
            matrix = np.zeros((numRows, colums), dtype=str)
            row = 0 
            col = 0 
            cham = 0
            for i in range(len(s)):
                matrix[row][col] = s[i]
                if cham < numRows - 1 : 
                    row += 1 
                    cham += 1
                else : 
                    row -= 1 
                    col += 1
                    if row == 0 : 
                        cham = 0 
            result = ""
            for i in range(numRows):
                for j in range(colums):
                    if matrix[i][j] != 0 :
                        result += matrix[i][j]
                print(result)
            return result   
                     
                
       
                
 
# ngoai ra bai toan con co the giai theo cach (khong can su dung ma tran de luu vao ban do zigzag ): 
# su dung list de luu tung row ( moi row la mot string va neu co khoang trang hay khong thi no van tra ve ket qua nhu the)          

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

    

    


if __name__ == "__main__":
    # Tạo object 
    solution = Solution()
    solution.convert("PAYPALISHIRING", 3)
    
    