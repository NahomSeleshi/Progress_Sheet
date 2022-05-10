class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.answer = []
        
        def dfs(currentList, currentSum, currentNumber):
            if currentSum > n:
                return
            if currentSum == n and len(currentList) == k:
                self.answer.append(currentList)
                return
            
            for i in range(currentNumber + 1, 10):
                tempList = copy.deepcopy(currentList)
                tempList.append(i)
                dfs(tempList, currentSum + i, i)
        
        dfs([], 0, 0)
        return self.answer
        
