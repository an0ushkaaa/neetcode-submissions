class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix) #number of rows
        n=len(matrix[0]) #number of columns
        for row in matrix:
            if row[n-1]<target: #last val of row is less than target
                continue
            elif row[n-1]>target: #last val of row is greater than target
                start=0
                end=n-1
                mid=(start+end)//2
                while start<=end:
                    if target==row[mid]:
                        return True
                    elif target>row[mid]:
                         start=mid+1
                         mid=(start+end)//2
                    elif target<row[mid]:
                         end=mid-1
                         mid=(start+end)//2
            else:
                return True
                
        return False


                


        