from scipy.spatial import ConvexHull


def convex_hull_3D(points):
    return ConvexHull(points)
