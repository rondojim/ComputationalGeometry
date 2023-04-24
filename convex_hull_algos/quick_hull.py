import sys

sys.path.append("../")

import utilities.geometry_utils as geom


def find_hull(S, P, Q, convex_hull):
    if not S:
        return []

    # find furthest point from line (P, Q)
    C = P
    for p in S:
        if geom.point_line_distance(P, Q, C) < geom.point_line_distance(P, Q, p):
            C = p

    # insert C between P and Q
    convex_hull.insert(convex_hull.index(P) + 1, C)
    S1 = []
    S2 = []

    # if p is in the triangle ignore
    # otherwise build S1 and S2
    # S1 points in one side
    # S2 on the other side
    for p in S:
        if geom.triangle_orientation(P, Q, C, p) <= 0:
            continue
        if geom.orientation(P, C, p) < 0:
            S1.append(p)
        else:
            S2.append(p)

    find_hull(S1, P, C, convex_hull)
    find_hull(S2, C, Q, convex_hull)


def Quick_hull(points):
    if len(points) <= 3:
        return points

    # find most left and most right points
    A = min(points)
    B = max(points)

    # add them to convex hull
    convex_hull = [A, B]
    S1 = []
    S2 = []

    for p in points:
        # if p is on the right side of A, B add to S1
        # if p is on the right side of B, A add to S2
        # if it is collinear ignore

        if geom.orientation(A, B, p) < 0:
            S1.append(p)
        elif geom.orientation(A, B, p) > 0:
            S2.append(p)

    find_hull(S1, A, B, convex_hull)
    find_hull(S2, B, A, convex_hull)

    return convex_hull
