import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d
import sys

sys.path.append("../../PartA/utilities")
sys.path.append("../utilities")

import testing_utils as tu

points = np.array(tu.random_point_set(10, 1, 100, False))
print(points)

tri = Delaunay(points)
vor = Voronoi(points)

plt.triplot(
    points[:, 0], points[:, 1], tri.simplices, "b-", label="Delaunay Triangulation"
)
voronoi_plot_2d(
    vor,
    show_vertices=False,
    line_colors="k",
    line_width=1,
    line_alpha=0.5,
    point_size=0.5,
    ax=plt.gca(),
    label="Voronoi Diagram",
)

plt.plot(points[:, 0], points[:, 1], "o", color="black")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Delaunay Triangulation and Voronoi Diagram")
plt.axis("equal")
plt.show()
