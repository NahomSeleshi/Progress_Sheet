class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        answer = []
        visited = [0 for _ in range(len(graph))]
        
        def dfs(i):
            possible = True
            if visited[i] == 1:
                return True
            if visited[i] == -1:
                return False
            
            visited[i] = -1
            for values in graph[i]:
                possible = dfs(values) and possible
            if possible:
                answer.append(i)
                visited[i] = 1
            return possible
        
        for i in range(len(graph)):
            dfs(i)
        answer.sort() 
        return answer
