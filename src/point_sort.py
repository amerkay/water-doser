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


class PointSort:
    @staticmethod
    def sort_points(points, use_simple_sort=False):
        """ Sort the points """
        if not use_simple_sort and len(points) > 0:
            # Get current location
            curr_pos = device.get_current_position()

            # this is for local debugging purposes, when running `python main.py`
            if curr_pos is None:
                curr_pos = {"x": 0, "y": 0}

            return PointSort.sort_points_by_dist(points, curr_pos)
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
        points_sorted = sorted(
            points, key=lambda elem: (int(elem["x"]), int(elem["y"]))
        )
        # log(points_sorted, title='sort_points')

        return points_sorted

    @staticmethod
    def _distance(p1, p2):
        """ Calculate distance between two points """
        dx = math.fabs(int(float(p1["x"])) - int(float(p2["x"])))
        dy = math.fabs(int(float(p1["y"])) - int(float(p2["y"])))
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

        # return sorted(points, key=lambda e: distance(e, target))

        totalDist = 0
        # tr = sorted(points, key=lambda elem: (int(elem['x']), int(elem['y'])))
        # bl = sorted(points, key=lambda elem: (int(elem['x']), int(-elem['y'])))
        # dist, cur = min([(PointSort._distance(start_point, p), p) for p in (tr[0], tr[-1], bl[0], bl[-1])])
        cur = start_point
        path = []
        for i in range(0, len(points)):
            dists = [(PointSort._distance(cur, p), p) for p in points if p not in path]
            nextDist, cur = min(dists, key=lambda t: t[0])
            totalDist += nextDist
            path.append(cur)

        log(
            "{} points sorted, total distance is {}".format(len(path), totalDist),
            title="sort_points_by_dist",
        )
        return path
