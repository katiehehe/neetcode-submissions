class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        start = newInterval[0]
        end = newInterval[1]
        newList = []
        for i in range(n):
            newList.append((intervals[i][0], i))
            newList.append((intervals[i][1], i))
        # binary search both endpoints
        # first find least greater than the starting point
        l = 0
        r = 2 * n
        while l < r:
            m = (l + r) // 2
            if newList[m][0] >= start:
                r = m
            else:
                l = m + 1
        # then find greatest smaller than end point
        l2 = -1
        r2 = 2 * n - 1
        while l2 < r2: 
            m2 = (l2 + r2 + 1) // 2
            if newList[m2][0] <= end:
                l2 = m2
            else:
                r2 = m2 - 1
        # now compare the intervals
        leftInt = r
        rightInt = l2
        print(f"{leftInt} and {rightInt}")
        # odd cases considered
        if leftInt == 2 * n:
            intervals.append(newInterval)
            return intervals
        if rightInt == -1:
            intervals.insert(0, newInterval)
            return intervals
        if leftInt > rightInt:
            print(rightInt)
            if newList[leftInt][1] == newList[rightInt][1]:
                return intervals
            intervals.insert(newList[leftInt][1], newInterval)
            return intervals
        # normal cases
        leftInd = newList[leftInt][1]
        rightInd = newList[rightInt][1]
        newInt = [min(intervals[leftInd][0], start), max(intervals[rightInd][1], end)]
        newLst = []
        for i in range(n):
            if i < leftInd or i > rightInd:
                newLst.append(intervals[i])
        # add the final interval
        newLst.insert(leftInd, newInt)
        return newLst
        

