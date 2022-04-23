class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        answer = []
        rowBegin, rowEnd = 0, len(matrix)-1
        columnBegin, columnEnd = 0, len(matrix[0])-1
        
        while(rowBegin <= rowEnd and columnBegin <= columnEnd):
            # this is to traverse to the right
            for i in range(columnBegin, columnEnd+1):
                answer.append(matrix[rowBegin][i])
            rowBegin += 1
            
            # this is to traverse down
            for j in range(rowBegin, rowEnd+1):
                answer.append(matrix[j][columnEnd])
            columnEnd -= 1
            
            if rowBegin <= rowEnd:
                # this is to traverse left
                for k in range(columnEnd, columnBegin-1, -1):
                    answer.append(matrix[rowEnd][k])
            rowEnd -= 1
            if columnBegin <= columnEnd:
                # this is to traverse up
                for l in range(rowEnd, rowBegin-1, -1):
                    answer.append(matrix[l][columnBegin])
            columnBegin += 1
            
        return answer
        
        
