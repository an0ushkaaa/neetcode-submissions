class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit=set()

        def dfs(row,column):
            if row>=len(grid) or column>=len(grid[0]) or row<0 or column<0 or grid[row][column]==0: 
                return 1
            if (row,column) in visit:
                return 0
            visit.add((row,column))
            perim=dfs(row,column+1)
            perim+=dfs(row+1,column)
            perim+=dfs(row-1,column)
            perim+=dfs(row,column-1)
            return perim

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column]:
                    return dfs(row,column)

        
                    