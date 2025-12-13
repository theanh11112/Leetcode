from typing import List

# ===== CHỖ NÀY BẠN TỰ VIẾT =====
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums :
            return 0 
        
        
        k = 0 
        for i in range(len(nums)) :
            if (nums[i] != val) :
                nums[k] = nums[i]
                k += 1
                
        return k 
                
               
                
                
            
        pass


# ===== TEST CASES (GIỐNG LEETCODE) =====
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 0, 1, 3, 4]),
        ([1], 1, []),
        ([1], 2, [1]),
        ([2, 2, 2], 2, []),
        ([], 1, []),
    ]

    for idx, (nums, val, expectedNums) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("Input nums:", nums)
        print("val:", val)

        k = solution.removeElement(nums, val)

        print("Returned k:", k)
        print("Expected k:", len(expectedNums))

        # Check k
        assert k == len(expectedNums), "❌ k is incorrect"

        # Vì thứ tự KHÔNG quan trọng → sort trước khi so
        nums_first_k = sorted(nums[:k])
        expected_sorted = sorted(expectedNums)

        for i in range(k):
            assert nums_first_k[i] == expected_sorted[i], f"❌ Wrong value at index {i}"

        print("Result nums (first k, sorted):", nums_first_k)
        print("✅ PASSED")
