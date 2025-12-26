# =========================
# 32. Longest Valid Parentheses
# =========================

class Solution(object):
    def longestValidParentheses(self, s):
        
        max_len = 0 
        stack = [-1]
        
        for i, ch in enumerate(s) :
            if ch == '(':
                stack.append(i)
            else :
                stack.pop()
                if not stack :
                    stack.append(i)
                else:
                    max_len = max(max_len,i - stack[-1])
                    
                        
        return max_len
                
                
                
            
            
            


# =========================
# TEST CASES (GIỐNG LEETCODE)
# =========================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            "(()",
            2
        ),

        # Example 2
        (
            ")()())",
            4
        ),

        # Example 3
        (
            "",
            0
        ),

        # Additional test cases
        (
            "()",
            2
        ),
        (
            "()(())",
            6
        ),
        (
            "(((((",
            0
        ),
        (
            ")))))",
            0
        ),
        (
            "()(()",
            2
        ),
        (
            ")()()(",
            4
        ),
        (
            "()()()",
            6
        ),
        (
            "(()())",
            6
        ),
    ]

    for idx, (s, expected) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("Input   :", repr(s))

        result = solution.longestValidParentheses(s)

        print("Returned:", result)
        print("Expected:", expected)

        assert result == expected, "❌ WRONG ANSWER"
        print("✅ PASSED")
