class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        deltas = [(1,0), (-1, 0), (0, 1), (0, -1)]
        starting_color = image[sr][sc]
                
        def dfs(r, c):
            row_boundary = 0 <= r < len(image)
            col_boundary = 0 <= c < len(image[0])
            if not row_boundary or not col_boundary or image[r][c] == color or image[r][c] != starting_color:
                return 
            image[r][c] = color
            for delta_row, delta_col in deltas:
                dfs(r + delta_row, c + delta_col)
        
        dfs(sr, sc)
        return image
        