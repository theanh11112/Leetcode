# =========================
# 43. Multiply Strings
# =========================

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # =========================
        # TODO: WRITE YOUR LOGIC HERE
        #
        # Yêu cầu:
        # - Không convert toàn bộ string sang int
        # - Không dùng BigInteger
        # - Time: O(m * n)
        # - Space: O(m + n)
        #
        # Gợi ý tư duy:
        # - Tạo mảng kết quả size m + n
        # - Nhân từng chữ số từ phải sang trái
        # - Đặt vào vị trí i + j + 1
        # - Xử lý carry
        # - Xoá số 0 đầu nếu có
        # =========================
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        m = len(num1)
        n = len(num2)
        
        result = [0] * (m +n)
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1 , -1):
                mul = int(num1[i]) * int(num2[j])
                sum_val = mul + result[i + j + 1]
                
                result[i + j + 1] = sum_val % 10
                result [i + j ] += sum_val // 10
            
        if result[0] == 0:
            result.pop(0)

        return ''.join(map(str, result))


# =========================
# TEST CASES – MULTIPLY STRINGS
# =========================
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Basic
        ("2", "3", "6"),
        ("123", "456", "56088"),

        # Zero cases
        ("0", "12345", "0"),
        ("999", "0", "0"),

        # Different lengths
        ("12", "10", "120"),
        ("100", "100", "10000"),

        # Large digits
        ("999", "999", "998001"),
        ("123456789", "9", "1111111101"),

        # Edge cases
        ("1", "1", "1"),
        ("1", "99999", "99999"),
    ]

    for idx, (num1, num2, expected) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("Input     :", num1, num2)

        result = solution.multiply(num1, num2)

        print("Returned  :", result)
        print("Expected  :", expected)

        assert result == expected, "❌ WRONG ANSWER"
        print("✅ PASSED")
