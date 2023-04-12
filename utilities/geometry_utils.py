import math

# computes orientation of points p, q, r using cross product's sign
# -1 -> clockwise
# 0 -> colinear
# 1 -> counter-clockwise


def orientation(p, q, r):
    cross_product = (q[0] - p[0]) * (r[1] - p[1]) - \
        (q[1] - p[1]) * (r[0] - p[0])
    if cross_product == 0:
        return 0
    return -1 if (cross_product < 0) else 1

# returns the slope of the line defined by point p and q
# if points are colinear 'inf' is returned


def slope(p, q):
    dx = float(q[0] - p[0])
    dy = float(q[1] - p[1])
    return (dy / dx) if (dx != 0) else float('inf')


# computes euclidean distance between two points
def distance(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)
