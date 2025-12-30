# =========================
# 35. Search Insert Position
# =========================

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # TODO:
        if not nums :
            return 0
        
        left, right = 0, len(nums) - 1 
        
        while left <= right :
            mid = (left + right ) // 2 
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else :
                right = mid -1 
        return right + 1 
          
    
       
    
     


# =========================
# TEST CASES (GIỐNG LEETCODE)
# =========================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [1,3,5,6],
            5,
            2
        ),

        # Example 2
        (
            [1,3,5,6],
            2,
            1
        ),

        # Example 3
        (
            [1,3,5,6],
            7,
            4
        ),

        # ===== Additional cases =====

        # Insert at beginning
        (
            [1,3,5,6],
            0,
            0
        ),

        # Insert at end
        (
            [1,3,5,6],
            10,
            4
        ),

        # Single element - found
        (
            [5],
            5,
            0
        ),

        # Single element - insert before
        (
            [5],
            2,
            0
        ),

        # Single element - insert after
        (
            [5],
            7,
            1
        ),

        # Empty array
        (
            [],
            3,
            0
        ),
    ]

    for idx, (nums, target, expected) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("Nums    :", nums)
        print("Target  :", target)

        result = solution.searchInsert(nums, target)

        print("Returned:", result)
        print("Expected:", expected)

        assert result == expected, "❌ WRONG ANSWER"
        print("✅ PASSED")
