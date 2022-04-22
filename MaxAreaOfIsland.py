# this question is solved below using dfs
class Solution:
    
    def dfs(self, row, column, grid):
        grid[row][column] = 0
        currentArea = 1
        if row > 0 and grid[row-1][column] == 1: 
            currentArea += self.dfs(row - 1, column, grid)
        if row < len(grid)-1 and grid[row + 1][column] == 1: 
            currentArea += self.dfs(row + 1, column, grid)
        if column > 0 and grid[row][column-1] == 1:
            currentArea += self.dfs(row, column - 1, grid)
        if column < len(grid[0])-1 and grid[row][column+1] == 1:
            currentArea += self.dfs(row, column + 1, grid)
        return currentArea
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maximumArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.maximumArea = max(self.maximumArea, self.dfs(i,j, grid))
                    
        return self.maximumArea
    
    
            
        
