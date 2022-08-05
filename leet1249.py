class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s1 = []
        chars = [c for c in s]
        for i , c in enumerate(chars):
            if c == '(' :
                s1.append(i)
            elif c == ')':
                if s1 :
                    s1.pop()
                else :
                    chars[i] = '*'
        while s1 : 
            chars[s.pop()]= '*'
        return ''.join(chars).replace('*','')