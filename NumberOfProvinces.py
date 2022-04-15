class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # In this code, I used union find to solve the problem
        
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]
        self.answer = n
        
        def findParent(node):
            if node == parent[node]:
                return node
            parent[node] = findParent(parent[node])
            return parent[node]
        
        def union(node1, node2):
            parent1 = findParent(node1)
            parent2 = findParent(node2)
            
            if parent1 != parent2:
                self.answer -= 1
            
            if rank[parent1] <= rank[parent2]:
                parent[parent1] = parent2
                rank[parent2] += 1
            else:
                parent[parent2] = parent1
                rank[parent1] += 1
        
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        return self.answer
        
