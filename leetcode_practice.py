# =========================
# 39. Combination Sum
# =========================

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []

        # =========================
        # TODO: WRITE YOUR LOGIC HERE
        #
        # Gợi ý (KHÔNG PHẢI CODE):
        # - Dùng backtracking
        # - Giữ start index
        # - Khi target == 0 → append kết quả
        # - Khi target < 0 → return
        # =========================
        
        def backtrack(start, path, remain):
            if remain == 0 :
                return result.append(path.copy())
            
            for i in range(start, len(candidates)):
                
                if candidates[i] > remain :
                    continue
                path.append(candidates[i])
                backtrack(i , path, remain - candidates[i])
                path.pop()

        backtrack(0, [], target)            
            

        return result


# =========================
# TEST CASES – COMBINATION SUM
# =========================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [2, 3, 6, 7],
            7,
            [[2,2,3], [7]]
        ),

        # Example 2
        (
            [2, 3, 5],
            8,
            [[2,2,2,2], [2,3,3], [3,5]]
        ),

        # Single candidate
        (
            [2],
            1,
            []
        ),

        # Exact match
        (
            [1],
            1,
            [[1]]
        ),

        # Multiple combinations
        (
            [2, 3],
            6,
            [[2,2,2], [3,3]]
        ),

        # No solution
        (
            [5, 10],
            3,
            []
        ),
    ]

    for idx, (candidates, target, expected) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("Candidates:", candidates)
        print("Target    :", target)

        result = solution.combinationSum(candidates, target)

        # sort để so sánh không phụ thuộc thứ tự
        result_sorted = sorted([sorted(r) for r in result])
        expected_sorted = sorted([sorted(e) for e in expected])

        print("Returned  :", result_sorted)
        print("Expected  :", expected_sorted)

        assert result_sorted == expected_sorted, "❌ WRONG ANSWER"
        print("✅ PASSED")
