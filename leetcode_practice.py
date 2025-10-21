from typing import List

class Solution(object):
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        Result = []
        n = len(nums)

        if n < 4:
            return []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    current_total = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_total < target:
                        left += 1
                    elif current_total > target:
                        right -= 1
                    else:
                        Result.append([nums[i], nums[j], nums[left], nums[right]])

                        # 🔁 Bỏ qua trùng lặp bên trái
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # 🔁 Bỏ qua trùng lặp bên phải
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Tiếp tục dịch hai con trỏ
                        left += 1
                        right -= 1

        return Result

# voi bai toan 4 con tro nay thi : 2 con tro co dinh , 2 con tro chay , chu khong the la 3 con tro cung chay 
# luu y neu choi i , j la 2 con tro co dinh chay song song thi se bi miss mat 1 so cap 
# nums = [1, 0, -1, 0, -2, 2] so cap i , j chay duoc la 5 
# nhung to hop so dien la C(6,2) = 15 so cap tat ca 
# giai thich luon li do tai sao co the xem i, j la 1 diem va co con tro ben trai va ben phai no se lam duoc nhung truong hop bi mat khi chung chay , nhung vi so con tro ben trai va ben phai khong du de 
if __name__ == "__main__":
    solution = Solution()

    # ✅ Các test case cho bài 4Sum
    test_cases = [
        # Mẫu cơ bản từ LeetCode
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),

        # Trường hợp có nhiều phần tử giống nhau
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),

        # Không có kết quả
        ([1, 2, 3, 4], 100, []),

        # Trường hợp với số âm
        ([-3, -1, 0, 2, 4, 5], 2, [[-3, -1, 2, 4]]),
    ]

    for idx, (nums, target, expected) in enumerate(test_cases, 1):
        result = solution.fourSum(nums, target)
        result_sorted = sorted([sorted(r) for r in result])
        expected_sorted = sorted([sorted(e) for e in expected])
        print(f"Test case {idx}: nums={nums}, target={target}")
        print(f"  👉 Expected: {expected_sorted}")
        print(f"  👉 Result:   {result_sorted}")
        print("✅ PASSED\n" if result_sorted == expected_sorted else "❌ FAILED\n")
