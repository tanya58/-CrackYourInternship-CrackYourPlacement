class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M,N = len(matrix),len(matrix[0])
        firstrow, firstcol = False, False
        for r in range(M):
            if matrix[r][0] == 0:
                firstcol = True
        for c in range(N):
            if matrix[0][c] == 0:
                firstrow = True
                
        for r in range(M):
            for c in range(1,N):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    
        for r in range(1,M):
            for c in range(1,N):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    
        for r in range(1,M):
            if matrix[r][0] == 0:
                matrix[r] = [0]*N
                
        for c in range(1,N):
            if matrix[0][c] == 0:
                for i in range(1,M):
                    matrix[i][c] = 0
                   
                    
        if firstrow:
            matrix[0] = [0]*N
        if firstcol:
            for i in range(M):
                matrix[i][0] = 0
                
        return matrix        
        
                

                
                 
            
                    
                     
                
            

                        
                        
        