class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit=set()
        rows,columns=len(grid),len(grid[0])
        q=collections.deque()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==0:
                    q.append((r,c))
                    visit.add((r,c))

        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                directions=[(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    nr,nc=dr+r,dc+c
                    if nr in range(rows) and nc in range(columns) and grid[nr][nc]==2147483647 and (nr,nc) not in visit:
                        grid[nr][nc]=dist+1
                        q.append((nr,nc))
                        visit.add((nr,nc))
            dist+=1


        
            
                


        