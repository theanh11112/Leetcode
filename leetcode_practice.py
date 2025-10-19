# leetcode_practice.py

"""
LeetCode Practice File
----------------------
Hướng dẫn:
1. Viết code trong class Solution theo yêu cầu của bài LeetCode.
2. Thêm test case trong phần main để chạy thử.
3. Chạy file bằng lệnh: python leetcode_practice.py
"""

from typing import List

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return None

        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            left, right = i - 1, i + 1
            while left >= 0 and right < len(nums):
                curr_sum = nums[left] + nums[i] + nums[right]

                # Cập nhật tổng gần nhất
                if abs(closest_sum - target) > abs(curr_sum - target):
                    closest_sum = curr_sum

                # Dịch con trỏ
                if curr_sum > target:
                    left -= 1
                elif curr_sum < target:
                    right += 1
                else:
                    return curr_sum  # Nếu trùng khớp hoàn hảo thì trả về luôn

        return closest_sum
# bai nay giai giong bai 3 tong o truoc nhung co dieu la khi tong = target thi return luon vi bai chi yeu cau tim tong gan target nhat 
# trong bai nay va ca bai truoc khi = 0 or = targer thi left -= 1 , right += 1 , la khong sai (mac du neu de xet so cap da duoc duyet thi miss mat 2 cap left; right +=1 , left -=1;right)
# nhung ko anh huong gi den bai toan 


if __name__ == "__main__":
    solution = Solution()

    # ✅ Các test case dành cho bài 3Sum Closest
    test_cases = [
        ([-1, 2, 1, -4], 1, 2),      # (-1 + 2 + 1 = 2)
        ([0, 0, 0], 1, 0),           # Tổng gần nhất = 0
        ([1, 1, 1, 0], -100, 2),     # Tổng nhỏ nhất = 0+1+1 = 2
        ([1, 1, 1, 0], 100, 3),      # Tổng lớn nhất = 1+1+1 = 3
        ([-3, -2, -5, 3, -4], -1, -2),  # Tổng gần nhất = -2
        ([0, 2, 1, -3], 1, 0),       # Tổng gần nhất = 0
    ]

    for idx, (nums, target, expected) in enumerate(test_cases, 1):
        result = solution.threeSumClosest(nums, target)
        print(f"Test case {idx}: nums = {nums}, target = {target}")
        print(f"  ➤ Kết quả mong đợi: {expected}")
        print(f"  ➤ Kết quả thực tế:  {result}")
        if result == expected:
            print("✅ PASSED\n")
        else:
            print("❌ FAILED\n")
