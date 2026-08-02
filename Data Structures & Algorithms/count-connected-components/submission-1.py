class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        count=n
        def find(x):
            while x!=parent[x]:
                x=parent[x]

            return x


        for u,v in edges:
            root1=find(u)
            root2=find(v)
            if root1!=root2:
                parent[root2]=root1
                count-=1

        return count