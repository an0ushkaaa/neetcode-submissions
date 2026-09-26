class Solution(object):
    def evalRPN(self, tokens):
        s = []

        for i in range(len(tokens)):
            if tokens[i] not in '+*/-':
                s.append(int(tokens[i]))
            else:
                a = s.pop()
                b = s.pop()

                if tokens[i] == '+':
                    ans = b + a
                elif tokens[i] == '*':
                    ans = b * a
                elif tokens[i] == '-':
                    ans = b - a
                else:
                    ans = int(b / a)

                s.append(ans)

        return s[-1]