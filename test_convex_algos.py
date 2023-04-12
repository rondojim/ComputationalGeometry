import convex_hull_algos.graham_scan as gs
import utilities.testing_utils as tut


def test_graham_scan():
    points = tut.random_point_set(80, 0, 1000)
    convex_hull = gs.Graham_scan(points)

    for p in convex_hull:
        print(f"{p[0]} {p[1]}")

    tut.plot_convex_hull(points, convex_hull)


test_graham_scan()
