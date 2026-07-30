class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        for ch in s :
            if ch == '{' or ch == "(" or ch == "[":
                stck.append(ch)
            else:
                if not stck:
                    return False
                top = stck.pop()
                if ch == '}' and top != "{":
                    return False
                elif ch == ')' and top != "(":
                    return False
                elif ch == ']' and top != '[':
                    return False
        return len(stck) == 0
