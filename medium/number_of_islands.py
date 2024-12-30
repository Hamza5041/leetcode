from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return 0


if __name__ == '__main__':
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    expected = 1
    actual = Solution().numIslands(grid)
    assert expected == actual, "\nactual: " + str(actual) + "\n" + "Expected: " + str(expected)