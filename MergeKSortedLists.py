# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop, heapify
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for list in lists:
            while list:
                minHeap.append(list.val)     
                list = list.next
        node = ListNode(0)
        answer = node
        heapify(minHeap)
        while minHeap:
            node.next = ListNode(heappop(minHeap))
            node = node.next
        return answer.next
