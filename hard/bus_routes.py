from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        pass

    def route_graph(self, routes: List[List[int]]) :
        adjList = {}
        for i, route in enumerate(routes):
            for stop in route:
                if stop not in adjList:
                    adjList[stop] = set()
                adjList[stop].add(i)
        return adjList






if __name__ == '__main__':
    routes = [[1,2,7],[3,6,7]]
    source = 1
    target =6

    solution = Solution()
    result = solution.numBusesToDestination(routes, source, target)
    # assert result == 2, "Output was not 2, it was: " + str(result)

    adjList = solution.route_graph(routes)
    print(adjList)
