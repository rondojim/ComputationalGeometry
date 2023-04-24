import sys

sys.path.append("../")

import utilities.geometry_utils as geom


# computes convex hull of points using graham scan algorithm
def Graham_scan(points):
    # set start of the convex hull as the most left and lowest point
    origin = min(points)

    # sort the points by slope around origin in counter-clockwise order
    # if two points have the same slope, sort by distance from origin
    points_sorted = sorted(
        points, key=lambda p: (geom.slope(origin, p), geom.distance(origin, p))
    )

    stack = [origin]
    for p in points_sorted:
        if p == origin:
            continue

        # while last two points and p are clockwise, remove last point
        while len(stack) >= 2 and geom.orientation(stack[-2], stack[-1], p) <= 0:
            stack.pop()

        stack.append(p)
    return stack
