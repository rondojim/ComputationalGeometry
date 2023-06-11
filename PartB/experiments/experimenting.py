import sys

sys.path.append("../../PartA/utilities")
sys.path.append("../utilities")

import testing_utils as tu
import kdtree as kd
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def plot_points(points, minx, maxx, miny, maxy, x_points):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    x_xvalues = [point[0] for point in x_points]
    x_yvalues = [point[1] for point in x_points]

    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values)
    ax.scatter(x_xvalues, x_yvalues, marker="x", color="black", s=75)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Plot of Points")

    rectangle = patches.Rectangle(
        (minx, miny),
        maxx - minx,
        maxy - miny,
        linewidth=1,
        edgecolor="r",
        facecolor="none",
    )
    ax.add_patch(rectangle)

    plt.show()


points = tu.random_point_set(60, 1, 20, False)
tree = kd.kdtree(points, 2)
minx = 5
maxx = 13
miny = 2
maxy = 17
in_rectangle = tree.search_rectangle(minx, maxx, miny, maxy)

print(points)
print(in_rectangle)

plot_points(points, minx, maxx, miny, maxy, in_rectangle)
