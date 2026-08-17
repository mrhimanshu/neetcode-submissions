class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        mapping = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in mapping.values(): #opening bracket
                a.append(i)
            elif i in mapping: # Closed bracket
                if not a or a[-1] != mapping[i]:
                    return False
                a.pop()
            else:
                return False

        return not a
        