class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prerequisitesForEach = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        answer = []
        
        for x,y in prerequisites:
            prerequisitesForEach[x].append(y)
        
        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            
            visited[i] = -1
            for each in prerequisitesForEach[i]:
                if not dfs(each):
                    return False
            visited[i] = 1
            answer.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return answer
