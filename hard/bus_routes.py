from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        pass

    def route_graph(self, routes: List[List[int]]) :

        # map stops to route
        # map which stop belongs to which bus route. This way you can find routes with shared buses
        stopsToRoutes = {}
        for i, route in enumerate(routes):
            for stop in route:
                if stop not in stopsToRoutes:
                    stopsToRoutes[stop] = set()
                stopsToRoutes[stop].add(i)

        # build connectingRoutes
        connectingRoutes = {}
        for stop, routes_at_stop in stopsToRoutes.items():
            for route1 in routes_at_stop:
                if route1 not in connectingRoutes:
                    connectingRoutes[route1] = set()
                connectingRoutes[route1].update(routes_at_stop - {route1})
        return connectingRoutes, stopsToRoutes






if __name__ == '__main__':
    routes = [[1,2,7],[3,6,7]]
    source = 1
    target =6

    solution = Solution()
    result = solution.numBusesToDestination(routes, source, target)
    # assert result == 2, "Output was not 2, it was: " + str(result)

    connectingRoutes, stopsToRoutes = solution.route_graph(routes)
    print(connectingRoutes)
    print(stopsToRoutes)
