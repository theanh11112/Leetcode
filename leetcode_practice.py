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
   def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start_point, end_point = 0, len(height) - 1
        max_area = 0  

        while start_point < end_point:
            width = end_point -start_point
            current_height = min(height[start_point], height[end_point])
            current_area = width * current_height   
            max_area = max(max_area, current_area)
            if height[start_point] < height[end_point]:
                start_point += 1
            else:
                end_point -= 1  
        return max_area 

         

                
    
            
                
        

  
    

if __name__ == "__main__":
    # Tạo object 
    solution = Solution()   
    # Test case 1                   
    height = [1,8,6,2,5,4,8,3,7]        
    print("Test case 1: ", solution.maxArea(height))  # Expected output: 49  