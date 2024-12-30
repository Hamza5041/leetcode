from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # standard bfs, checks for connected components
        numOfIslands = 0
        # directions to check
        directions = [ [1,0], [-1,0], [0,1], [0,-1]]
        rows, columns = len(grid), len(grid[0])

        # need to do bfs on each node for connected components
        # every iteraction of the while loop means a new connected component (island)
        for r in range(rows):
            for c in range(columns):
                # found start of next connected component
                if grid[r][c] == "1":
                    numOfIslands += 1
                    # initialize the queue and add the first node found
                    queue = deque([(r,c)])
                    # main bfs
                    while queue:
                        # pop off row and column from queue
                        currentRow, currentColumn = queue.popleft()
                        # if the row and column is valid (within range), and it is land (==1) explore it
                        if 0 <= currentRow < rows and 0 <= currentColumn < columns and grid[currentRow][currentColumn] == "1":
                            # instead of using a set, mark the grid directly to keep track
                            grid[currentRow][currentColumn] = "0"
                            # add neighbors to be explored
                            for dr,dc in directions:
                                nextRow, nextColum = currentRow + dr, currentColumn + dc
                                queue.append((nextRow, nextColum))





        return numOfIslands


if __name__ == '__main__':
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    expected = 3
    actual = Solution().numIslands(grid)
    assert expected == actual, "\nactual: " + str(actual) + "\n" + "Expected: " + str(expected)