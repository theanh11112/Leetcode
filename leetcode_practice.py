# ===== CHỖ NÀY BẠN TỰ VIẾT =====
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
     
        if divisor == 0 :
            return None
        
        if (dividend == INT_MIN and divisor == -1) :
            return INT_MAX
        
        
        negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        
        result = 0 
        temp = dividend
        temp1 = divisor
        k= 0 
        
        while (temp >= temp1):
              k = 0 
              while (temp >= (temp1 << k)):
                  k += 1  
              result += (1 << (k - 1))
              temp  -= (temp1 << (k - 1))           
                
        if (negative) :
            return -result 
        else :
            return result 
        
            
        
                
        
            
            
            
        
        
            
        
        
        pass   # 🚫 KHÔNG VIẾT THUẬT TOÁN Ở ĐÂY


# ===== TEST CASES (GIỐNG LEETCODE) =====
if __name__ == "__main__":
    solution = Solution()

    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    test_cases = [
        # basic
        (10, 3, 3),
        (7, -3, -2),
        (-7, 3, -2),
        (-7, -3, 2),

        # divisible
        (8, 2, 4),
        (-8, 2, -4),
        (8, -2, -4),

        # dividend = 0
        (0, 1, 0),
        (0, -1, 0),

        # divisor = 1 / -1
        (5, 1, 5),
        (5, -1, -5),
        (-5, 1, -5),
        (-5, -1, 5),

        # edge 32-bit
        (INT_MIN, 1, INT_MIN),
        (INT_MAX, 1, INT_MAX),

        # overflow case (QUAN TRỌNG)
        (INT_MIN, -1, INT_MAX),

        # small numbers
        (1, 1, 1),
        (-1, 1, -1),
        (1, -1, -1),

        # larger
        (100, 9, 11),
        (-100, 9, -11),
    ]

    for idx, (dividend, divisor, expected) in enumerate(test_cases, 1):
        print(f"\nTest {idx}")
        print("dividend:", dividend)
        print("divisor:", divisor)

        result = solution.divide(dividend, divisor)

        print("Returned:", result)
        print("Expected:", expected)

        assert result == expected, "❌ WRONG ANSWER"
        print("✅ PASSED")
