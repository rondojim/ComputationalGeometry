import sys

sys.path.append("../")

from utilities import geometry_utils as geom


def divide(points):
    N = len(points)
    LN = int((N / 2) if (N % 2 == 0) else ((N + 1) / 2))

    points_sorted = sorted(points)
    return points_sorted[:LN], points_sorted[LN:]


def merge_hulls(left_hull, right_hull):
    LN = len(left_hull)
    RN = len(right_hull)

    A = aidx = left_hull.index(max(left_hull))
    B = bidx = right_hull.index(min(right_hull))

    upper_tangent = False
    while upper_tangent == False:
        upper_tangent = True

        # while there are points of left hull above the tangent,
        #       or points collinear, move A up
        while (
            geom.orientation(right_hull[B], left_hull[A], left_hull[(A + 1) % LN]) <= 0
        ):
            A = (A + 1) % LN
            upper_tangent = False
        # while there are points of right hull above the tangent,
        #       or points collinear, move B up
        while (
            geom.orientation(left_hull[A], right_hull[B], right_hull[(B - 1 + RN) % RN])
            >= 0
        ):
            B = (B - 1 + RN) % RN
            upper_tangent = False

    upperA = A
    upperB = B

    A = aidx
    B = bidx
    lower_tangent = False

    while lower_tangent == False:
        lower_tangent = True

        # while there are points of left hull below the tangent,
        #       or points collinear, move A down
        while (
            geom.orientation(right_hull[B], left_hull[A], left_hull[(A - 1 + LN) % LN])
            >= 0
        ):
            A = (A - 1 + LN) % LN
            lower_tangent = False
        # while there are points of right hull above the tangent,
        #       or points collinear, move B up
        while (
            geom.orientation(left_hull[A], right_hull[B], right_hull[(B + 1) % RN]) <= 0
        ):
            B = (B + 1) % RN
            lower_tangent = False
    lowerA = A
    lowerB = B

    convex_hull = [left_hull[upperA]]
    while upperA != lowerA:
        upperA = (upperA + 1) % LN
        convex_hull.append(left_hull[upperA])

    convex_hull.append(right_hull[lowerB])
    while lowerB != upperB:
        lowerB = (lowerB + 1) % RN
        convex_hull.append(right_hull[lowerB])

    return convex_hull


def DC_convex_hull(points):
    # if we have less than 6 points, then if we divide
    #       at least one hull will be a line or a point
    #       so we solve it with "brute force"
    if len(points) <= 5:
        return geom.convex_hull_brute(points)

    L, R = divide(points)
    left_hull = DC_convex_hull(L)
    right_hull = DC_convex_hull(R)
    return merge_hulls(left_hull, right_hull)
