import random
import matplotlib.pyplot as plt


# creates a set of N random points in [lb, ub] x [lb, ub]
#       with integer coordinates
def random_point_set(N, lb, ub, no_same_X):
    points_set = set()

    xs = []
    if no_same_X:
        xs = random.sample(range(lb, ub + 1), N)
    else:
        xs = random.choices(range(lb, ub + 1), k=N)

    for x in xs:
        y = random.randint(lb, ub)

        while (x, y) in points_set:
            y = random.randint(lb, ub)

        points_set.add((x, y))

    return list(points_set)


# creates a set of N point, with many collinear
#       in [lb, ub] x [lb, ub] with integer coordinates
# T controls the probability to generate 3 collinear points in each step
# low T -> higher probability


def random_collinear(N, lb, ub, T, no_same_X):
    points_set = set()

    xs = []
    if no_same_X:
        xs = random.sample(range(lb, ub + 1), N)
    else:
        xs = random.choices(range(lb, ub + 1), k=N)

    for x in xs:
        y = random.randint(lb, ub)
        while (x, y) in points_set:
            y = random.randint(lb, ub)

        points_set.add((x, y))
        collinear = random.randint(0, T)

        if collinear == 0:
            dx = random.randint(int((ub - x) / 4), int((ub - x) / 2))
            dy = random.randint(int((ub - y) / 4), int((ub - y) / 2))

            if dx == 0 and no_same_X == True:
                continue

            if random.randint(0, 2) == 0 and no_same_X == True:
                dx = 0
            if random.randint(0, 2) == 0 and dx != 0:
                dy = 0

            for m in range(2):
                if len(points_set) < N:
                    xx = x + dx * (m + 1)
                    yy = y + dy * (m + 1)
                    points_set.add((x, y))

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
