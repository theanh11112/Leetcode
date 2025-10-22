# leetcode_practice.py

"""
LeetCode Practice File
----------------------
Hướng dẫn:
1. Viết code trong class Solution theo yêu cầu của bài LeetCode.
2. Thêm test case trong phần main để chạy thử.
3. Chạy file bằng lệnh: python leetcode_practice.py
"""

import numpy as np



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] 
        mapping = { ")": "(", "}": "{", "]": "[" }
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else :
                stack.append(char)
        return not stack 

#     if char in mapping: la so sanh theo key chu khong phai so sanh theo value 
#    mapping = { ")": "(", "}": "{", "]": "[" }  tao 1 dict de luu tru key va value           
         
   

if __name__ == "__main__":

    # Tạo object 
    solution = Solution()   
    # Test case 1  
    s1 = "()"
    print("Test case 1: ", solution.isValid(s1))  # Kết quả đúng: True            

    # Test case 2   
    s2 = "()[]{}"
    print("Test case 2: ", solution.isValid(s2))  # Kết quả đúng: True  
    # Test case 3   
    s3 = "(]"
    print("Test case 3: ", solution.isValid(s3))  # Kết quả đúng: False  
    # Test case 4   
    s4 = "([)]"             
    print("Test case 4: ", solution.isValid(s4))  # Kết quả đúng: False 
   