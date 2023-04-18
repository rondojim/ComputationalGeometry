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
