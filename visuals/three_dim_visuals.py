import sys

sys.path.append("../")

import convex_hull_algos.three_dim_scipy_lib as td
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

lb, ub = 0, 100
N = 50

# create unique points
points = []
while len(points) < N:
    new_points = np.random.randint(lb, ub + 1, size=(N - len(points), 3))
    new_points = np.unique(new_points, axis=0)
    points.extend(new_points)

points = np.array(points)
lst = [tuple(ar) for ar in list(points)]
print(lst)

# use 3D convex hull from scipy (quick hull)
convex_hull = td.convex_hull_3D(points)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c="black", marker="o")

hull_verts = []
# loop through simplices
# "Indices of points forming the simplical facets of the convex hull"
for simplex in convex_hull.simplices:
    # append start of simplex to close shape
    simplex = np.append(simplex, simplex[0])
    ax.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], "r-")
    hull_verts.append(points[simplex, :])


def update(angle):
    ax.view_init(elev=30, azim=angle)
    return (ax,)


# use vertices to create Poly3D object to fill it
hull_collection = Poly3DCollection(hull_verts, alpha=0.3, facecolor="gray")
ax.add_collection(hull_collection)

# Create an animation object that updates the plot for each frame
ani = FuncAnimation(fig, update, frames=180, interval=50)
writer = PillowWriter(fps=15)
ani.save("3D_convex_hull.gif", writer=writer)
plt.show()
