import sys
sys.path.append('../')

import utilities.geometry_utils as geom


def Jarvis(points):
    N = len(points)

    if N <= 2:
        return points

    # find index of most left and lowest point
    lowest = points.index(min(points))
    r0 = lowest
    convex_hull = []

    while True:
        convex_hull.append(points[r0])
        q = (r0 + 1) % N

        for i in range(N):
            orient = geom.orientation(points[r0], points[i], points[q])
            
            # check if i is more clockwise than q
            if (orient > 0 or (orient == 0 and
                               (geom.distance(points[r0], points[i]) > geom.distance(points[r0], points[q])))):
                q = i

        r0 = q
        if r0 == lowest:
            break
    
    return convex_hull
