class Solution:
    def merge(self, intervals):
        intervals.sort()
        sol = []

        for cur in intervals:
            if not sol or sol[-1][1] < cur[0]:
                sol.append(cur)
            else:
                sol[-1][1] = max(sol[-1][1], cur[1])


        return sol