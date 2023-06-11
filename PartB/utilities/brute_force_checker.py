def check_kd_tree_result(points, in_rectangle, a, b, c, d):
    bf_result = [
        p for p in points if a <= p[0] and p[0] <= b and c <= p[1] and p[1] <= d
    ]

    bf_result = sorted(bf_result)
    in_rectangle_ = sorted(in_rectangle)

    return bf_result == in_rectangle_
