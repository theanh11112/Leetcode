# =========================
# 40. Combination Sum II
# =========================

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        candidates.sort()   # 🔑 BẮT BUỘC: để skip trùng & break sớm

        def backtrack(start, path, remain):
            # 🎯 Thu hoạch
            if remain == 0:
                result.append(path.copy())
                return

            for i in range(start, len(candidates)):
                # ❌ Skip số trùng trong cùng tầng
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # 🚫 Cắt nhánh sớm (vì đã sort)
                if candidates[i] > remain:
                    break

                # 👉 Chọn số hiện tại
                path.append(candidates[i])

                # 🔁 Không dùng lại số → i + 1
                backtrack(i + 1, path, remain - candidates[i])

                # 👈 Hoàn tác
                path.pop()

        backtrack(0, [], target)
        return result


# =========================
# TEST CASES – COMBINATION SUM II
# =========================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1 (LeetCode)
        (
            [10, 1, 2, 7, 6, 1, 5],
            8,
            [[1,1,6], [1,2,5], [1,7], [2,6]]
        ),

        # Example 2 (LeetCode)
        (
            [2, 5, 2, 1, 2],
            5,
            [[1,2,2], [5]]
        ),

        # Single element
        (
            [1],
            1,
            [[1]]
        ),

        # Duplicates only
        (
            [1, 1],
            2,
            [[1,1]]
        ),

        # Multiple same numbers
        (
            [3, 3, 3],
            3,
            [[3]]
        ),

        # No solution
        (
            [5, 10],
            3,
            []
        ),

        # Larger case
        (
            [1,1,1,2,2,3],
            4,
            [[1,1,2], [1,3], [2,2]]
        ),
    ]

    for idx, (candidates, target, expected) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("Candidates:", candidates)
        print("Target    :", target)

        result = solution.combinationSum2(candidates, target)

        # sort để so sánh không phụ thuộc thứ tự
        result_sorted = sorted([sorted(r) for r in result])
        expected_sorted = sorted([sorted(e) for e in expected])

        print("Returned  :", result_sorted)
        print("Expected  :", expected_sorted)

        assert result_sorted == expected_sorted, "❌ WRONG ANSWER"
        print("✅ PASSED")
