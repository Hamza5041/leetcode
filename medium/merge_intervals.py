from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        end = float('-inf')
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            print(i)
            if intervals[i][0] < merged[-1][1]:
                merged[-1][1] = intervals[i][1]
            else:
                merged.append(intervals[i])
        return merged






if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    expected = [[1,6],[8,10],[15,18]]

    result = Solution().merge(intervals)
    print("\nresult: " + str(result) + "\n" + "Expected: " + str(expected))
    # assert result == intervals, "\nresult: " + str(result) + "\n" + "Expected: " + str(expected)