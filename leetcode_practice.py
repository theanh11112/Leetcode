# =========================
# 41. First Missing Positive
# =========================

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # =========================
        # TODO: WRITE YOUR LOGIC HERE
        #
        # Yêu cầu bắt buộc:
        # - Time: O(n)
        # - Space: O(1)
        # - Không dùng set / map / array phụ
        # - Không sort
        #
        # Gợi ý tư duy (KHÔNG PHẢI CODE):
        # - Mỗi số x (1 ≤ x ≤ n) có "ghế" tại index x-1
        # - Đưa số về đúng ghế nếu có thể
        # - Sau đó duyệt tìm ghế trống đầu tiên
        # =========================
        
        i = 0 
        n = len(nums)
        
        while i < n:
            x = nums[i]
            
            if 1 <= x <= n and x != nums[x - 1]:
                nums[i] , nums[x - 1] = nums[x - 1], nums[i]
            else: 
                i += 1
                  

        for i in range (len(nums)):
            if nums[i] != i + 1 :
                return i + 1 
        return len(nums) + 1 
                 


# =========================
# TEST CASES – FIRST MISSING POSITIVE
# =========================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Basic cases
        (
            [1, 2, 0],
            3
        ),
        (
            [3, 4, -1, 1],
            2
        ),
        (
            [7, 8, 9, 11, 12],
            1
        ),

        # Edge cases
        (
            [1],
            2
        ),
        (
            [2],
            1
        ),
        (
            [],
            1
        ),

        # Duplicates
        (
            [1, 1],
            2
        ),
        (
            [2, 2],
            1
        ),

        # Mixed
        (
            [2, 1],
            3
        ),
        (
            [0, -1, 3, 1],
            2
        ),
        (
            [1, 2, 3],
            4
        ),
    ]

    for idx, (nums, expected) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("Input     :", nums)

        result = solution.firstMissingPositive(nums[:])  # copy để tránh side-effect

        print("Returned  :", result)
        print("Expected  :", expected)

        assert result == expected, "❌ WRONG ANSWER"
        print("✅ PASSED")