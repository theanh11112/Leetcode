from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy 

        while prev.next and prev.next.next : 
            first = prev.next 
            second = prev.next.next

            first.next = second.next
            second.next = first 
            prev.next = second 

            prev = first 

        return dummy.next 
    


# bai toan binh thuong nhung len su dung dummy de giai quyet de khong bi miss truong hop , ngoai ra moi tro lai lam viec voi listnode len hoi ngao 1 chu 
#       


    


       


# ====== HELPER FUNCTIONS ======
def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for v in arr[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ====== TEST CASES ======
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([1, 2, 3], [2, 1, 3]),
        ([1], [1]),
        ([], []),
        ([1, 2], [2, 1]),
        ([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
    ]

    for idx, (input_list, expected) in enumerate(test_cases, 1):
        head = build_list(input_list)
        result_head = solution.swapPairs(head)
        result_arr = list_to_array(result_head)

        print(f"\nTest {idx}: input = {input_list}")
        print(f"  Expected: {expected}")
        print(f"  Result:   {result_arr}")
        print("  👉 PASSED" if result_arr == expected else "  ❌ FAILED")
