# leetcode_practice.py

"""
LeetCode Practice File
----------------------
Hướng dẫn:
1. Viết code trong class Solution theo yêu cầu của bài LeetCode.
2. Thêm test case trong phần main để chạy thử.
3. Chạy file bằng lệnh: python leetcode_practice.py
"""

import numpy as np
class ListNode(object):
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Solution(object):
         
   def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        dummy = ListNode(0, head)
        fastnode = dummy
        slownode = dummy

        for i in range(n):
           if fastnode:
              fastnode = fastnode.next
           else : 
              return head 
          
        while fastnode.next:
             fastnode = fastnode.next
             slownode = slownode.next  
        slownode.next = slownode.next.next
        
        return dummy.next
            

        


if __name__ == "__main__":

    # Tạo object 
    solution = Solution()   
    # Test case 1   
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Input:", [1,2,3,4,5], "n=2")
    new_head = solution.removeNthFromEnd(head, 2)
    print("Output:", print_linked_list(new_head))  # ✅ [1,2,3,5]

    # Test 2 - xóa node đầu tiên
    head = ListNode(1, ListNode(2))
    print("Input:", [1,2], "n=2")
    new_head = solution.removeNthFromEnd(head, 2)
    print("Output:", print_linked_list(new_head))  # ✅ [2]

    # Test 3 - list chỉ có 1 node
    head = ListNode(1)
    print("Input:", [1], "n=1")
    new_head = solution.removeNthFromEnd(head, 1)
    print("Output:", print_linked_list(new_head))  # ✅ []

    # Test 4 - xóa node cuối
    head = ListNode(1, ListNode(2, ListNode(3)))
    print("Input:", [1,2,3], "n=1")
    new_head = solution.removeNthFromEnd(head, 1)
    print("Output:", print_linked_list(new_head))  # ✅ [1,2]
    


