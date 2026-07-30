class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stk.append(int(t))
            else:
                n1 = stk.pop()
                n2 = stk.pop()

                if t == "+":
                    stk.append(n2 + n1)
                elif t == "-":
                    stk.append(n2 - n1)
                elif t == "*":
                    stk.append(n2 * n1)
                else:  
                    stk.append(int(n2 / n1))

        return stk[-1]