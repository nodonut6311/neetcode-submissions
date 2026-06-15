class Solution:
    def checkValidString(self, s: str) -> bool:
        mino = maxo = 0

        for char in s:

            if char == '(':
                mino += 1
                maxo += 1

            elif char == ')':
                mino -= 1
                maxo -= 1

            else: 
                mino -= 1
                maxo += 1

            if maxo < 0:
                return False

            mino = max(mino, 0)

        return mino == 0