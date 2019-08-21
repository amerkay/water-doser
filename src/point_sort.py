""" PointSort class

Includes static-methods for sorting points by (x, y) coordinates.

Variables:
    log {method} -- A reference function Logger().log()
"""

import math

from farmware_tools import device

# import static logger and create shortcut function
from logger import Logger
log = Logger.log


class PointSort():
    @staticmethod
    def sort_points(points, use_tsp_solver=True):
        """ Sort the points """
        if (use_tsp_solver is True) and len(points) > 0:
            # Get current location
            currpos = {'x': 0, 'y': 0} if device.get_current_position() is None else device.get_current_position()
            log("current position is {}".format(currpos), title="sort_points")
            return PointSort.sort_points_by_dist(points, currpos)
        else:
            return PointSort.sort_points_basic(points)

    @staticmethod
    def sort_points_basic(points):
        """ Sort points using basic x, y sorting.

        Arguments:
            points {list of Points} -- A list of Celeryscript Point JSON objects (sets)

        Returns:
            {list of Points} -- The sorted list of Celeryscript Point JSON objects (sets)
        """
        points_sorted = sorted(points, key=lambda elem: (int(elem['x']), int(elem['y'])))
        # log(points_sorted, title='sort_points')

        return points_sorted

    @staticmethod
    def _distance(p1, p2):
        """ Calculate distance between two points """
        dx = math.fabs(p1['x'] - p2['x'])
        dy = math.fabs(p1['y'] - p2['y'])
        return math.hypot(dx, dy)

    @staticmethod
    def sort_points_by_dist(points, start_point):
        """ Sort points using Travelling Salesman Greedy Solution

        Source: https://github.com/etcipnja/MLH

        Arguments:
            points {list of Points} -- A list of Celeryscript Point JSON objects (dicts)

        Returns:
            {list of Points} -- The sorted list of Celeryscript Point JSON objects (dicts)
        """
        if len(points) < 1:
            return []

        totalDist = 0
        tr = sorted(points, key=lambda elem: (int(elem['x']), int(elem['y'])))
        bl = sorted(points, key=lambda elem: (int(elem['x']), int(-elem['y'])))
        dist, cur = min([(PointSort._distance(start_point, p), p) for p in (tr[0], tr[-1], bl[0], bl[-1])])
        path = [cur]
        for i in range(1, len(points)):
            dists = [(PointSort._distance(cur, p), p) for p in points if p not in path]
            nextDist, cur = min(dists, key=lambda t: t[0])
            totalDist += nextDist
            path.append(cur)

        log("points sorted, total distance is {}".format(totalDist), title="sort_points_by_dist")
        return path
