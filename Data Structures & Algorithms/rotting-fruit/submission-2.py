class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,columns=len(grid),len(grid[0])
        q=deque()
        fresh=0
        v=set()
        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==2:
                    q.append((r,c))
                    v.add((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        time=-1
        while q:
            
            
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            for i in range(len(q)):
                
                r,c=q.popleft()
                for dr,dc in directions:
                    nr,nc=dr+r,dc+c
                    if nr in range(rows) and nc in range(columns) and grid[nr][nc]==1 and (nr,nc) not in v:
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        v.add((r,c))
                        
            time+=1
        for row in grid:
            if 1 in row:
                return -1
        if fresh==0:
            return 0
                        


        return time