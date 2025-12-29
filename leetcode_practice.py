# =========================
# 34. Find First and Last Position of Element in Sorted Array
# =========================

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums :
            return [-1, -1]
        # TODO: Bạn tự viết thuật toán ở đây
        result = [-1, -1]
        left, right = 0 , len(nums) - 1
        
        while left <= right :
            mid = (left + right) // 2
            if nums[mid] == target:
                result[0] = mid      
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        left, right = 0 , len(nums) - 1      
        while left <= right :
            mid = (left + right) // 2
            if nums[mid] == target:
                result[1] = mid      
            if nums[mid] > target:
                 right = mid - 1
            else:
                left = mid + 1
           
                
            
        return result


# =========================
# TEST CASES (GIỐNG LEETCODE)
# =========================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [5,7,7,8,8,10],
            8,
            [3,4]
        ),

        # Example 2
        (
            [5,7,7,8,8,10],
            6,
            [-1,-1]
        ),

        # Example 3
        (
            [],
            0,
            [-1,-1]
        ),

        # ===== Additional cases =====

        # Single element - found
        (
            [1],
            1,
            [0,0]
        ),

        # Single element - not found
        (
            [1],
            0,
            [-1,-1]
        ),

        # All elements are target
        (
            [2,2,2,2,2],
            2,
            [0,4]
        ),

        # Target at beginning
        (
            [3,4,5,6,7],
            3,
            [0,0]
        ),

        # Target at end
        (
            [3,4,5,6,7],
            7,
            [4,4]
        ),

        # Multiple occurrences in middle
        (
            [1,2,3,3,3,4,5],
            3,
            [2,4]
        ),

        # Target not present
        (
            [1,2,3,4,5],
            6,
            [-1,-1]
        ),
    ]

    for idx, (nums, target, expected) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("Nums    :", nums)
        print("Target  :", target)

        result = solution.searchRange(nums, target)

        print("Returned:", result)
        print("Expected:", expected)

        assert result == expected, "❌ WRONG ANSWER"
        print("✅ PASSED")
