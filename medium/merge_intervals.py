from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        print(intervals)






if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    expected = [[1,6],[8,10],[15,18]]

    result = Solution().merge(intervals)
    # assert result == intervals, "\nresult: " + str(result) + "\n" + "Expected: " + str(expected)