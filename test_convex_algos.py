import convex_hull_algos.graham_scan as gs
import convex_hull_algos.jarvis as jr
import convex_hull_algos.divide_and_conquer as dc
import convex_hull_algos.quick_hull as qh

import utilities.testing_utils as tut


def test_graham_scan():
    points = tut.random_point_set(80, 0, 1000, False)
    convex_hull = gs.Graham_scan(points)

    tut.plot_convex_hull(points, convex_hull, "Graham Scan")


def test_jarvis():
    points = tut.random_point_set(80, 0, 1000, False)
    convex_hull = jr.Jarvis(points)

    tut.plot_convex_hull(points, convex_hull, "Jarvis")


def test_divide_and_conquer():
    points = tut.random_point_set(80, 0, 1000, True)
    convex_hull = dc.DC_convex_hull(points)

    tut.plot_convex_hull(points, convex_hull, "Divide and Conquer")


def test_quick_hull():
    points = tut.random_point_set(80, 0, 1000, False)
    convex_hull = qh.Quick_hull(points)

    tut.plot_convex_hull(points, convex_hull, "Quick Hull")


# test_graham_scan()
# test_jarvis()
# test_divide_and_conquer()
test_quick_hull()
