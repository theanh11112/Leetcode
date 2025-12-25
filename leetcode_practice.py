# =========================
# 31. Next Permutation
# =========================

# ===== CHỖ NÀY BẠN TỰ VIẾT =====
class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1:
            return

        # 1️⃣ tìm pivot
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2️⃣ swap pivot với số nhỏ nhất > pivot
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 3️⃣ reverse đoạn sau pivot
        l, r = i + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
    
# =========================
# TEST CASES (GIỐNG LEETCODE)
# =========================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [1, 2, 3],
            [1, 3, 2]
        ),

        # Example 2
        (
            [3, 2, 1],
            [1, 2, 3]
        ),

        # Example 3
        (
            [1, 1, 5],
            [1, 5, 1]
        ),

        # Edge cases
        (
            [1],
            [1]
        ),
        (
            [1, 3, 2],
            [2, 1, 3]
        ),
        (
            [2, 3, 1],
            [3, 1, 2]
        ),
        (
            [1, 5, 1],
            [5, 1, 1]
        ),
        (
            [5, 4, 3, 2, 1],
            [1, 2, 3, 4, 5]
        ),
        (
            [1, 2, 2, 3],
            [1, 2, 3, 2]
        ),
    ]

    for idx, (nums, expected) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("Input   :", nums)

        solution.nextPermutation(nums)

        print("Returned:", nums)
        print("Expected:", expected)

        assert nums == expected, "❌ WRONG ANSWER"
        print("✅ PASSED")
