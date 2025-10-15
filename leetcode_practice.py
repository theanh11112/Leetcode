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
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # a , b = len(s) -1  , len(p) -1 

        # while a >= 0  and  b >= 0 :
        #     if s[a] == p[b] or p[b] == '.':
        #         a -= 1
        #         b -= 1
        #     elif p[b] == '*' : 
        #         if p[b-1] == '.' or b == 0:
        #             return True
        #         else :
        #             while a >= 0 and s[a] == p[b-1]:
        #                 a -= 1
        #             b -= 2
        #     else :
        #         return False
        # return a < 0 and b < 0 

        # truong hop dau tien ky tu do la ky tu thuong or . thi bat ki ky tu nao cung duoc de tiep tuc 
        # truong hop thu 2 : ky tu do la * : 
        # + neu truoc do la ky tu thuong : thi co the bo qua 0 or >= 1 ky tu do 
        # + neu truoc do la . : thi co the bo qua 0 or >= 1 ky tu do
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(2 , n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2] # '*' can eliminate the preceding element

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i -1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]

                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]

    # bai hard trong leet code su dung tu duy quy hoach dong de giai quyet 
    # mang 2d dung de luu cac trang thai d[i][j] : voi cach suy nghi chinh la : d[i][j] de mo ta cho trang thai i-1 va j-1 
    # neu d[i][j] = True : tuc la s[0:i-1] va p[0:j-1] la match nhau    
    # va giai quyet duoc truong hop j-1 = * thi se co 2 truong hop
    # truong hop 1 : p[j-2] khong duoc su dung : d[i][j] = d[i][j-2]
    # truong hop 2 : p[j-2] duoc su dung : d[i][j] = d  [i-1][j] neu p[j-2] == s[i-1] or p[j-2] == '.'  
    # trang thai sau se phu thuoc vao trang thai truoc do len can phai su dung mang quy hoach dong de luu trang thai 
                    
    
            
                
        

  
    

if __name__ == "__main__":
    # Tạo object 
    solution = Solution()
    print(solution.isMatch("a", "*a"))  # ✅ ĐÚNG: True | ❌ CODE TRẢ: False

    # ❌ LỖI 2: '*' lặp nhiều lần (code chỉ bỏ hết, không thử lặp nhiều)
    # "aaa" vs "a*a" -> "a*" match "aa", rồi "a" cuối match nốt -> True
    print(solution.isMatch("aaa", "a*a"))  # ✅ ĐÚNG: True | ❌ CODE TRẢ: False

    # ❌ LỖI 3: '.' kèm '*' (.*) ở giữa chuỗi
    # "a.*d" có thể match "abcd"
    print(solution.isMatch("abcd", "a.*d"))  # ✅ ĐÚNG: True | ❌ CODE TRẢ: True (nhưng sai logic, luôn True kể cả "abcx")

    # ✅ thử chứng minh lỗi logic trên:
    print(solution.isMatch("abcx", "a.*d"))  # ✅ ĐÚNG: False | ❌ CODE TRẢ: True

    # ❌ LỖI 4: Pattern dài hơn s, và có thể bỏ bớt ký tự nhờ '*'
    # "a" vs "ab*" -> b* có thể là "" → True
    print(solution.isMatch("a", "ab*"))  # ✅ ĐÚNG: True | ❌ CODE TRẢ: False

    # ❌ LỖI 5: Pattern có * ở đầu (truy cập p[b-1] sẽ lỗi nếu b == 0)
    # "*a" là regex không hợp lệ (phải return False hoặc báo lỗi)
    try:
        print(solution.isMatch("a", "*a"))  # ✅ ĐÚNG: False | ❌ CODE crash IndexError
    except Exception as e:
        print("LỖI 5: pattern bắt đầu bằng * gây crash:", e)

    # ❌ LỖI 6: Pattern kết thúc bằng * mà không cần ký tự sau đó
    # "aaa" vs "a*" -> hợp lệ, vì "a*" có thể match hết "aaa"
    print(solution.isMatch("aaa", "a*"))  # ✅ ĐÚNG: True | ❌ CODE TRẢ: False

    # ✅ ĐÚNG (code match đúng)
    print(solution.isMatch("ab", ".*"))  # ✅ True — code đúng trường hợp này
    
    
    