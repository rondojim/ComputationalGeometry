import random
import matplotlib.pyplot as plt


# creates a set of N random points in [lb, ub] x [lb, ub]
#       with integer coordinates
def random_point_set(N, lb, ub, no_same_X):
    points_set = set()
    Xs = set()

    while len(points_set) < N:
        x = random.randint(lb, ub)
        y = random.randint(lb, ub)

        if no_same_X == True and (x in Xs):
            continue

        points_set.add((x, y))
        Xs.add(x)

    return list(points_set)


# plots points
def plot_points(points):
    plt.scatter([p[0] for p in points], [p[1] for p in points])


#  plots convex hull of a set of points
def plot_convex_hull(points, convex_hull, algo):
    plot_points(points)

    for i in range(len(convex_hull)):
        p1 = convex_hull[i]
        p2 = convex_hull[(i + 1) % len(convex_hull)]
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color="r")

    plt.title(f"Convex hull using {algo} with {len(points)} points")
    plt.show()
