# =========================
# 33. Search in Rotated Sorted Array
# =========================

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) -1
        
        while left <= right :
            mid = (left + right ) // 2
            if (nums[mid] == target):
                return mid
            
            if nums[left] <= nums[mid] :
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1 
            else :
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else :
                    right = mid - 1
                    
                
        return -1    
          
                
                
            
                
                
            
        pass


# =========================
# TEST CASES (GIỐNG LEETCODE)
# =========================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [4,5,6,7,0,1,2],
            0,
            4
        ),

        # Example 2
        (
            [4,5,6,7,0,1,2],
            3,
            -1
        ),

        # Example 3
        (
            [1],
            0,
            -1
        ),

        # ===== Additional cases =====

        # No rotation
        (
            [1,2,3,4,5],
            3,
            2
        ),

        # Rotated at middle
        (
            [6,7,1,2,3,4,5],
            4,
            5
        ),

        # Target at beginning
        (
            [5,6,7,1,2,3,4],
            5,
            0
        ),

        # Target at end
        (
            [5,6,7,1,2,3,4],
            4,
            6
        ),

        # Target is pivot
        (
            [3,4,5,6,7,1,2],
            1,
            5
        ),

        # Array of size 2
        (
            [3,1],
            1,
            1
        ),

        # Array of size 2 - not found
        (
            [3,1],
            2,
            -1
        ),

        # Fully rotated (same as original)
        (
            [1,2,3,4,5],
            6,
            -1
        ),
    ]

    for idx, (nums, target, expected) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("Nums   :", nums)
        print("Target :", target)

        result = solution.search(nums, target)

        print("Returned:", result)
        print("Expected:", expected)

        assert result == expected, "❌ WRONG ANSWER"
        print("✅ PASSED")
