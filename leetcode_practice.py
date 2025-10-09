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

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        a , b = 0 , 0 
        substring = [] 
        for i in range(len(s)) :
            a , b = i , i 
            while a >= 0 and b < len(s) and s[a] == s[b] : 
                a -= 1 
                b += 1 
            print(a ,b )
            if b - a - 1 > len(substring) :
                substring = s[a + 1  : b ]

            a , b = i , i + 1  
            while a >= 0 and b < len(s) and s[a] == s[b] : 
                a -= 1 
                b += 1 
            print(a ,b )
            if b - a - 1 > len(substring) :
                substring = s[a + 1  : b ]

            

        return substring
                
 
           

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

    

    


if __name__ == "__main__":
    # Tạo object 
    solution = Solution()
    print(solution.longestPalindrome("babad"))
    
    