# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        numFrequency = defaultdict(int)
        numbers = []
        
        while head:
            numFrequency[head.val] += 1
            head = head.next
        
        for key in numFrequency:
            if numFrequency[key] == 1:
                numbers.append(key)
        node1 = ListNode(0)
        answer = node1
        
        for value in numbers:
            node1.next = ListNode(value)
            node1 = node1.next
        
        return answer.next
