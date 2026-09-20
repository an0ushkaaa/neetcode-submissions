class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s1=[]
        for i in s:
            if i.isalnum():
                s1.append(i)
        s1=''.join(s1)
        print(s,s1)
        print(s1[::-1])
        if s1[::-1]==s1:
            return True
        else:
            return False
        