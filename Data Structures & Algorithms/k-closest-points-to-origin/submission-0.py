
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis=[]
        ans=[]
        for i in points:
            dis.append((i[0]**2 + i[1]**2,i))
        heapq.heapify(dis)
        for j in range(k):
            ans.append(heapq.heappop(dis)[1])
        
        return ans
        