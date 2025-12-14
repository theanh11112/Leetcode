from typing import List

# ===== CHỖ NÀY BẠN TỰ VIẾT =====
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "" :
            return 0
        
        k = 0
        for i in range(len(haystack)) :
            while (k < len(needle) and i + k < len(haystack) and haystack[i + k] == needle[k] ):
                if ( k == (len(needle) - 1)):
                    return i 
                else :
                    k += 1
            k = 0
        return -1  
                 
               
            
        
    
                
               
                
                
            
    

# ===== TEST CASES (GIỐNG LEETCODE) =====
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("abc", "abc", 0),
        ("abc", "c", 2),
        ("abc", "d", -1),
        ("mississippi", "issi", 1),
        ("mississippi", "issip", 4),
        ("a", "a", 0),
        ("a", "b", -1),
    ]

    for idx, (haystack, needle, expected) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("haystack:", haystack)
        print("needle:", needle)

        result = solution.strStr(haystack, needle)

        print("Returned:", result)
        print("Expected:", expected)

        assert result == expected, "❌ WRONG ANSWER"
        print("✅ PASSED")
