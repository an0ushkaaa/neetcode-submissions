class Solution:
    def countSeniors(self, details: List[str]) -> int:
        s=0
        for i in details:
            if (int(i[11])*10)+int(i[12])>60:
                s+=1
        return s
        