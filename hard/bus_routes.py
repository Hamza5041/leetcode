from queue import Queue
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        adjList = self.route_graph(routes)

        queue = Queue()
        visited = set()

        # add all the routes connected to the source from the adj list
        for route in adjList.get(source):
            queue.put(route)
            visited.add(route)

        buses = 1
        # BFS
        while not queue.empty():
            # deque the current route ready in the queue
            currentRoute = queue.get()
            # check the routes array for stops. If the stop is the target, return the buses it took to get there
            for stop in routes[currentRoute]:
                if stop == target:
                    return buses
                # otherwise, queue all the routes for each stop into the queue and mark as visited if they have not been
                for nextRoute in adjList.get(stop):
                    if nextRoute not in visited:
                        visited.add(nextRoute)
                        queue.put(nextRoute)
            # increment buses taken at each iteration
            buses += 1
        return -1



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
    assert result == 2, "Output was not 2, it was: " + str(result)

    adjList = solution.route_graph(routes)
    print(adjList)
