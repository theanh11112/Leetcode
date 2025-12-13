from typing import List

# ===== CHỖ NÀY BẠN TỰ VIẾT =====
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
       if not nums :
           return 0
        
        
       k = 1 
       for i in range(1, len(nums)) :
           if (nums[i] != nums[k - 1]):
               nums[k] = nums [i]
               k += 1 
               
       return k


# ===== TEST CASES (GIỐNG LEETCODE) =====
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
        ([1, 1, 1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([1], [1]),
        ([], []),
    ]

    for idx, (nums, expectedNums) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("Input nums:", nums)

        k = solution.removeDuplicates(nums)

        print("Returned k:", k)
        print("Expected k:", len(expectedNums))

        # Check k
        assert k == len(expectedNums), "❌ k is incorrect"

        # Check first k elements
        for i in range(k):
            assert nums[i] == expectedNums[i], f"❌ Wrong value at index {i}"

        print("Result nums (first k):", nums[:k])
        print("✅ PASSED")
