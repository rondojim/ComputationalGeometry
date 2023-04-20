import sys

sys.path.append("../")

from utilities import geometry_utils as geom
import utilities.testing_utils as tut

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter


def divide(points):
    N = len(points)
    LN = int((N / 2) if (N % 2 == 0) else ((N + 1) / 2))

    points_sorted = sorted(points)
    return points_sorted[:LN], points_sorted[LN:], points_sorted[LN - 1][0]


def merge_hulls(left_hull, right_hull, steps_keep):
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
    upperA_ = upperA
    upperB_ = upperB

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
    lowerA_ = lowerA
    lowerB_ = lowerB

    steps_keep.append(
        (
            3,
            (
                (left_hull[upperA_], right_hull[upperB_]),
                (left_hull[lowerA_], right_hull[lowerB_]),
            ),
        )
    )

    convex_hull = [left_hull[upperA]]
    while upperA != lowerA:
        upperA = (upperA + 1) % LN
        convex_hull.append(left_hull[upperA])

    convex_hull.append(right_hull[lowerB])
    while lowerB != upperB:
        lowerB = (lowerB + 1) % RN
        convex_hull.append(right_hull[lowerB])

    steps_keep.append((-2, (left_hull, right_hull)))
    steps_keep.append(
        (
            -3,
            (
                (left_hull[upperA_], right_hull[upperB_]),
                (left_hull[lowerA_], right_hull[lowerB_]),
            ),
        )
    )
    steps_keep.append((2, convex_hull))
    return convex_hull


def DC_convex_hull(points, steps_keep):
    # if we have less than 6 points, then if we divide
    #       at least one hull will be a line or a point
    #       so we solve it with "brute force"
    if len(points) <= 5:
        ch = geom.convex_hull_brute(points)
        steps_keep.append((2, ch))
        return ch

    L, R, middle = divide(points)
    steps_keep.append((1, middle))
    left_hull = DC_convex_hull(L, steps_keep)
    right_hull = DC_convex_hull(R, steps_keep)
    steps_keep.append((-1, middle))
    return merge_hulls(left_hull, right_hull, steps_keep)


N = 16
lb = 0
ub = 100

points = tut.random_point_set(N, lb, ub, True)

fig, ax = plt.subplots()

lines = set()
steps_keep = []

DC_convex_hull(points, steps_keep)
points = np.array(points)


def animate(frame):
    plt.cla()
    if frame == 0:
        lines.clear()
    ax.set_xlim([lb - (int)((ub - lb) / 10), ub + (int)((ub - lb) / 10)])
    ax.set_ylim([lb - (int)((ub - lb) / 10), ub + (int)((ub - lb) / 10)])
    ax.scatter(points[:, 0], points[:, 1], color="lightgray", edgecolor="k", alpha=0.6)

    step = steps_keep[frame]
    if step[0] == 1:
        # Add vertical
        lines.add(((step[1], lb), (step[1], ub), "v"))
    elif step[0] == 2:
        # Add polygon
        for i in range(len(step[1])):
            j = (i + 1) % len(step[1])
            p1 = min(step[1][i], step[1][j])
            p2 = max(step[1][i], step[1][j])
            lines.add((p1, p2, "p"))
    elif step[0] == 3:
        # Add tangent
        for t in range(2):
            p1 = min(step[1][t][0], step[1][t][1])
            p2 = max(step[1][t][0], step[1][t][1])
            lines.add((p1, p2, "t"))
    elif step[0] == -1:
        # Remove vertical
        lines.remove(((step[1], lb), (step[1], ub), "v"))
    elif step[0] == -2:
        # Remove polygon
        left_hull = step[1][0]
        for h in range(2):
            for i in range(len(step[1][h])):
                j = (i + 1) % len(step[1][h])
                p1 = min(step[1][h][i], step[1][h][j])
                p2 = max(step[1][h][i], step[1][h][j])
                lines.remove((p1, p2, "p"))
    else:
        # Remove tangent
        for t in range(2):
            p1 = min(step[1][t][0], step[1][t][1])
            p2 = max(step[1][t][0], step[1][t][1])
            lines.remove((p1, p2, "t"))

    for p1, p2, t in lines:
        if t == "v":
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], "r--")
        elif t == "p":
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], "g")
        elif t == "t":
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], "b:")
    return []


ani = FuncAnimation(fig, animate, frames=len(steps_keep), interval=500)
writer = PillowWriter(fps=2)
ani.save("DivideAndConquerDemo.gif", writer=writer)
plt.show()
