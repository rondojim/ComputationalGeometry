import convex_hull_algos.graham_scan as gs
import convex_hull_algos.jarvis as jr

import utilities.testing_utils as tut


def test_graham_scan():
    points = tut.random_point_set(80, 0, 1000)
    convex_hull = gs.Graham_scan(points)

    tut.plot_convex_hull(points, convex_hull, "Graham Scan")

def test_jarvis():
    points = tut.random_point_set(80, 0, 1000)
    convex_hull = jr.Jarvis(points)

    tut.plot_convex_hull(points, convex_hull, "Jarvis")

test_graham_scan()
test_jarvis()
