from typing import List
from queue import Queue


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # standard bfs, checks for connected components
        numOfIslands = 0
        queue = Queue()
        visited = set()
        rows, columns = len(grid), len(grid[0])

        # need to do bfs on each node for connected components
        # every iteraction of the while loop means a new connected component (island
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visited:
                    numOfIslands += 1
                    # add the first node to queue and visited
                    queue.put((r, c))
                    visited.add((r, c))
                    # main bfs
                    while not queue.empty():
                        # pop off next row and column to explore
                        currentRow, currentColumn = queue.get()
                        # directions to check
                        directions = [ [1,0], [-1,0], [0,1], [0,-1]]
                        for dr,dc in directions:
                            nextRow, nextColum = currentRow + dr, currentColumn + dc
                            # check if  the nextRow and next column is within the range of rows and columns
                            # then check if it is an valid land aka == 1
                            # then check if it has been visited or not
                            if 0 <= nextRow < rows and 0 <= nextColum < columns and grid[nextRow][nextColum] == "1" and (nextRow, nextColum) not in visited:
                                queue.put((nextRow, nextColum))
                                visited.add((nextRow,nextColum))




        return numOfIslands


if __name__ == '__main__':
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    expected = 3
    actual = Solution().numIslands(grid)
    assert expected == actual, "\nactual: " + str(actual) + "\n" + "Expected: " + str(expected)