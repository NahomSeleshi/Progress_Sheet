# this problem is solved using dynamic programming
class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = [0 for i in range(len(nums))]
        visited = set()
        def dfs(index):
            if index >= len(nums):
                return 0
            if index in visited:
                return memo[index]
            
            rob = nums[index] + dfs(index + 2)
            notRob = dfs(index + 1)
            maxMoney = max(rob, notRob)
            memo[index] = maxMoney
            visited.add(index)
            return maxMoney
        return dfs(0)
        
        
