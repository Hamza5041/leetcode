from queue import Queue
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0



        adjList = self.route_graph(routes)

        if source not in adjList or target not in adjList:
            return -1

        queue = Queue()
        visited = set()

        # add all the routes connected to the source from the adj list
        for route in adjList.get(source):
            queue.put(route)
            visited.add(route)

        buses = 1
        # BFS
        while not queue.empty():
            for _ in range(queue.qsize()):
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
    routes = [[1,9,12,20,23,24,35,38],[10,21,24,31,32,34,37,38,43],[10,19,28,37],[8],[14,19],[11,17,23,31,41,43,44],[21,26,29,33],[5,11,33,41],[4,5,8,9,24,44]]
    source = 37
    target =28

    solution = Solution()
    result = solution.numBusesToDestination(routes, source, target)
    assert result == 1, "Output was not 1, it was: " + str(result)

    adjList = solution.route_graph(routes)
    print(adjList)
