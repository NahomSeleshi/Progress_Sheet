class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prerequisitesForEach = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x,y in prerequisites:
            prerequisitesForEach[x].append(y)
        
        def dfs(i):
            # this means we reach to a course that is in a group of courses we are 
            # currently visiting and we form a cycle
            if visited[i] == -1:
                return False
            
            # this means we reach to a course that we previously visited and know that we
            # can proceed after this course by taking another courses without forming a cycle
            if visited[i] == 1:
                return True
            
            # we mark courses we are currently visiting as -1 and if we get another -1,
            # then there is a cycle which results we cannot take those group of courses
            
            visited[i] = -1
            
            for values in prerequisitesForEach[i]:
                if not dfs(values):
                    return False
                
            # all courses marked with 1 are courses with no cycle and we mark them as 1
            # after we check if we can take the group of courses containing i with no cycle
            
            visited[i] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
