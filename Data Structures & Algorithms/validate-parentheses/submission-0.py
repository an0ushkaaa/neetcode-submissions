class Solution(object):
    def isValid(self, s):
        stack=[]
        for i in s:
                if i=='(' or i=='[' or i=='{':
                     stack.append(i)
                     top=i
                else:
                    if len(stack)==0:
                        stack.append(i)
                        top=i
                    elif i==')' and top=='(' or i==']' and top=='[' or i=='}' and top=='{':
                       stack.pop()
                       if len(stack)!=0:
                           top=stack[-1]
                    else:
                        return False

        if len(stack)==0:
                 return True
        else:
                return False
       

       
        