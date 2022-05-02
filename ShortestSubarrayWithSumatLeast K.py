class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
    
        temp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            temp[i + 1] = temp[i] + nums[i]
            
        deque = collections.deque()
        res = len(nums) + 1
        
        for i in range(len(nums) + 1):
            
            while deque and temp[i] - temp[deque[0]] >= k: 
                res = min(res, i - deque.popleft())
            
            while deque and temp[i] <= temp[deque[-1]]: 
                deque.pop()
            
            deque.append(i)
        
        return res if res <= len(nums) else -1
                
