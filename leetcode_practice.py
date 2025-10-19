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
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    # khi lam viec voi 1 mang so nguyen thi can kiem tra xem mang do co can sap xep de co the nang cao hieu suat 
    # b1 : sap xep mang , sau do kiem tra tu 1 -> n-3 de xem tong > 0 neu > 0 thi bo 3 so cuoi khong the la dap an (vi mang da duoc sap xep)
    # su dung two point de kiem tra tu 2 phia voi moi 1 diem dang xet 
    # su dung two point co the khac phuc duoc van de lap lai diem
        result: List[List[int]] = []
        nums.sort()
        
        for i in range(1,len(nums)):
             left, right = i - 1, i + 1
             while left >= 0 and right < len(nums)  :
                 sum = nums[left] + nums[i] + nums[right]
                 if (sum == 0):
                     triplet = sorted([nums[left], nums[i], nums[right]])
                     if triplet not in result:
                         result.append(triplet)
                     left -= 1 
                     right += 1
                 elif(sum > 0):
                     left -= 1
                 else:
                     right += 1
        return result
            
                     
             

        


        
    
                
        

  
    

if __name__ == "__main__":
    # Tạo object 
    solution = Solution()   
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([], []),
        ([0], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([1, -1, -1, 0], [[-1, 0, 1]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 4, 4, 6, 6], [[-4, -2, 6], [-4, 0, 4], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]),
    ]

    # Kiểm tra từng test case
    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = solution.threeSum(nums)
        result_sorted = sorted([sorted(triplet) for triplet in result])
        expected_sorted = sorted([sorted(triplet) for triplet in expected])

        print(f"Test case {idx}: nums = {nums}")
        print(f"  ➤ Kết quả mong đợi: {expected_sorted}")
        print(f"  ➤ Kết quả thực tế:  {result_sorted}")
        if result_sorted == expected_sorted:
            print("✅ PASSED\n")
        else:
            print("❌ FAILED\n")
 
