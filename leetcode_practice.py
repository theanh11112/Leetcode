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
import heapq
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = [] 

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i , node = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next 
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next 
    
# thay vi phai quan ly K con tro, ta them chi so i vao heap de tranh viec so sanh giua cac ListNode khong hop le
# heap se luu vao 1 tupple (node.val, i, node) de dam bao tinh duy nhat khi so sanh 
# khi pop ra thi lay duoc ca chi so i de biet duoc node thuoc list nao, va de tranh truong hop loi khi cac node co gia tri giong nhau ma khong co i de so sanh se sinh ra loi 
     
    
    

if __name__ == "__main__":

    # Tạo object 
    solution = Solution()   
    # Test case 1
    list1 = ListNode(1, ListNode(4, ListNode(5)))   
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))
    lists = [list1, list2, list3]
    merged_head = solution.mergeKLists(lists)
    # In kết quả
    current = merged_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
    # Test case 2
    lists = []
    merged_head = solution.mergeKLists(lists)
    print(merged_head)  # Expected output: None
    # Test case 3
    lists = [None]
    merged_head = solution.mergeKLists(lists)
    print(merged_head)  # Expected output: None
    # Thêm các test case khác nếu cần
    # Test case 4
    list1 = ListNode(2)
    lists = [list1]
    merged_head = solution.mergeKLists(lists)
    current = merged_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
    
 