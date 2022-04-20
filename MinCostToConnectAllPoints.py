# this code implements both union find and min heap concepts
from heapq import heappop, heappush

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.minimumCost = 0
        
        # here I used a heap to implement Kruskal's algorithm where I always want to pick 
        # the edge with minimum weight
        minHeap = []
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                manhattan_distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heappush(minHeap, [manhattan_distance,i,j])
                 
        parent = [i for i in range(len(points))]
        rank = [1 for i in range(len(points))]
        
        def findParent(node):
            if node == parent[node]:
                return node
            parent[node] = findParent(parent[node])
            return parent[node]
        
        def union(node1, node2):
            parent1 = findParent(node1)
            parent2 = findParent(node2)
            
            if parent1 != parent2:
                self.minimumCost += temp[0]
                if rank[parent1] <= rank[parent2]:
                    parent[parent1] = parent2
                    rank[parent2] += rank[parent1]
                    rank[parent1] = 0
                else:
                    parent[parent2] = parent1
                    rank[parent1] += rank[parent2]
                    rank[parent2] = 0
                    
        maxChildren = 0
        while maxChildren != len(points) and minHeap:
            temp = heappop(minHeap)
            union(temp[1], temp[2])
            maxChildren = max(maxChildren, max(rank))
            
        return self.minimumCost
        
        
