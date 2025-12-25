# ===== CHỖ NÀY BẠN TỰ VIẾT =====
from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words :
            return [] 
        
        word_len = len(words[0])
        total_len = len(words) * word_len
        need = Counter(words)
        result = []
        
        for offset in range(word_len):
            
            left = offset 
            right = offset
            window = {}
            count = 0 
            
            while right + word_len <= len(s) :
                
                word = s[right : right + word_len]
                
                if word not in need :
                    window.clear()
                    right += word_len
                    left = right 
                    count = 0
                    continue 
                      
                window[word] = window.get(word, 0) + 1
                count += 1 
                right += word_len
                
                
                while window[word] > need[word] :
                    left_word = s[left : left + word_len]
                    window[left_word] = window.get(left_word, 0) - 1
                    count -= 1 
                    left +=  word_len
                    
                if (count == len(words)):
                    result.append(left)
                    left_word = s[left : left + word_len]
                    window[left_word] = window.get(left_word, 0) - 1 
                    left += word_len
                    count -= 1 
                    
                    
        return result         
                
      


# ===== TEST CASES (GIỐNG LEETCODE) =====
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            "barfoothefoobarman",
            ["foo", "bar"],
            [0, 9]
        ),

        # Example 2
        (
            "wordgoodgoodgoodbestword",
            ["word", "good", "best", "word"],
            []
        ),

        # Example 3
        (
            "barfoofoobarthefoobarman",
            ["bar", "foo", "the"],
            [6, 9, 12]
        ),

        # edge cases
        (
            "",
            ["a"],
            []
        ),
        (
            "aaaaaa",
            ["aa", "aa"],
            [0, 1, 2]
        ),
        (
            "foobar",
            ["foo", "bar"],
            [0]
        ),
        (
            "foobarfoo",
            ["foo", "bar"],
            [0, 3]
        ),
    ]

    for idx, (s, words, expected) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("s:", s)
        print("words:", words)

        result = solution.findSubstring(s, words)

        print("Returned:", result)
        print("Expected:", expected)

        assert sorted(result) == sorted(expected), "❌ WRONG ANSWER"
        print("✅ PASSED")
