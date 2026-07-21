class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visit=set()
        rows,columns=len(grid),len(grid[0])
        island=0

        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                r,c=q.popleft()
                directions=[(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    if (r+dr) in range(rows) and (c+dc) in range(columns) and grid[(r+dr)][(c+dc)]=='1' and ((r+dr),(c+dc)) not in visit:
                        q.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))
                        print(q)
                        print(visit)




        for r in range(rows):
            for c in range(columns):
                if grid[r][c]=='1' and (r,c) not in visit:
                    bfs(r,c)
                    island+=1
        return island