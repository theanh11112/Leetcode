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

class Solution(object):
   def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        result = [""] 

        if not digits:
            return []
        for i in digits:
                currents = []
                for k in result:
                    for m in digit_to_char[i]:
                        currents.append(k + m)
                result = currents
        return result
   
                    
                
                    

     
        



if __name__ == "__main__":
    solution = Solution()

    # ✅ Các test case dành cho bài 3Sum Closest
    test_cases = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
        ("9", ["w", "x", "y", "z"]),
    ]
    for idx, (digits, expected) in enumerate(test_cases, 1):
        result = solution.letterCombinations(digits)
        print(f"Test case {idx}: digits = '{digits}'")
        print(f"  ➤ Kết quả mong đợi: {expected}")
        print(f"  ➤ Kết quả thực tế:  {result}")
        if sorted(result) == sorted(expected):
            print("✅ PASSED\n")
        else:
            print("❌ FAILED\n")
   