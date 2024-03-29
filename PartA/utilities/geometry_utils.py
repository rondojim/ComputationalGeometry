import math


# computes orientation of points p, q, r using cross product's sign
# -1 -> clockwise
# 0 -> colinear
# 1 -> counter-clockwise
def orientation(p, q, r):
    cross_product = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    if cross_product == 0:
        return 0
    return -1 if (cross_product < 0) else 1


# returns the slope of the line defined by point p and q
# if points are colinear 'inf' is returned
def slope(p, q):
    dx = float(q[0] - p[0])
    dy = float(q[1] - p[1])
    return (dy / dx) if (dx != 0) else float("inf")


# computes euclidean distance between two points
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# computes euclidean distance between the point r and the line passing from p and q
def point_line_distance(p, q, r):
    triangle_area = 0.5 * abs(
        (q[0] - p[0]) * (p[1] - r[1]) - (p[0] - r[0]) * (q[1] - p[1])
    )
    pq_distance = distance(p, q)

    return 2 * triangle_area / pq_distance


# computes orientation of s in respect of the triangle formed by p, q, and r
# -1 -> inside
# 0 -> on edge
# 1 -> outside
def triangle_orientation(p, q, r, s):
    a = orientation(p, q, s)
    b = orientation(q, r, s)
    c = orientation(r, p, s)

    if abs(a + b + c) == 3:
        return -1
    if (
        (point_line_distance(p, q, s) < 1e-6)
        or (point_line_distance(q, r, s) < 1e-6)
        or (point_line_distance(r, p, s) < 1e-6)
    ):
        return 0
    return 1


# brute force for computing convex hull
def convex_hull_brute(points):
    hull = set()

    if len(points) > 3:
        # if all points are on the same side of the line created from
        #       p1 and p2 then add both points to hull
        for p1 in points:
            for p2 in points:
                if p1 == p2:
                    continue

                neg_orient = pos_orient = 0
                coll = False
                for p3 in points:
                    if (p3 == p1) or (p3 == p2):
                        continue
                    orient = orientation(p1, p2, p3)
                    neg_orient += 1 if orient < 0 else 0
                    pos_orient += 1 if orient > 0 else 0

                    if orient == 0:
                        # check if it is outside of segment
                        if (distance(p1, p3) + distance(p2, p3)) > (
                            distance(p1, p2) + 1e-6
                        ):
                            coll = True
                if ((neg_orient == 0) or (pos_orient == 0)) and (coll == False):
                    hull.add(p1)
                    hull.add(p2)
        hull = list(hull)
    else:
        hull = list(points)

    origin = min(hull)
    hull_sorted = sorted(hull, key=lambda p: (slope(origin, p), distance(origin, p)))

    return hull_sorted


# checks if convex hull solution is correct
def check_convex_hull(result, points):
    correct = True

    # for each point check if it is inside or on the polygon
    if len(result) < 3:
        return False

    for p in points:
        if p in result:
            continue
        pos_orient = 0
        neg_orient = 0
        on_orient = 0

        for i in range(len(result)):
            j = (i + 1) % len(result)
            if orientation(result[i], result[j], p) > 0:
                pos_orient += 1
            elif orientation(result[i], result[j], p) < 0:
                neg_orient += 1
            else:
                on_orient += 1

        if not (on_orient > 0 or (pos_orient * neg_orient == 0)):
            correct = False
            break

    # check that the polygon is convex
    # check that no collinear points appear
    pos_orient = 0
    neg_orient = 0
    on_orient = 0

    for i in range(len(result)):
        j = (i + 1) % len(result)
        k = (i + 2) % len(result)

        if orientation(result[i], result[j], result[k]) > 0:
            pos_orient += 1
        elif orientation(result[i], result[j], result[k]) < 0:
            neg_orient += 1
        else:
            on_orient += 1

    if not (on_orient == 0 and (pos_orient * neg_orient == 0)):
        correct = False

    return correct
