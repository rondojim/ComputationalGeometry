import sys

sys.path.append("../")

import convex_hull_algos.graham_scan as gs
import convex_hull_algos.jarvis as jr
import convex_hull_algos.divide_and_conquer as dc
import convex_hull_algos.quick_hull as qh

import utilities.geometry_utils as geom
import utilities.testing_utils as tut


def test_correctness_graham_scan(points):
    convex_hull = gs.Graham_scan(points)
    print(convex_hull)

    if geom.check_convex_hull(convex_hull, points) == False:
        print("Graham Scan error")
    else:
        tut.plot_convex_hull(points, convex_hull, "Graham Scan")


def test_correctness_jarvis(points):
    convex_hull = jr.Jarvis(points)
    print(convex_hull)

    if geom.check_convex_hull(convex_hull, points) == False:
        print("Jarvis error")
    else:
        tut.plot_convex_hull(points, convex_hull, "Jarvis")


def test_correctness_divide_and_conquer(points):
    convex_hull = dc.DC_convex_hull(points)
    print(convex_hull)

    if geom.check_convex_hull(convex_hull, points) == False:
        print("Divide and Conquer error")
    else:
        tut.plot_convex_hull(points, convex_hull, "Divide and Conquer")


def test_correctness_quick_hull(points):
    convex_hull = qh.Quick_hull(points)
    print(convex_hull)

    if geom.check_convex_hull(convex_hull, points) == False:
        print("Quick hull error")
    else:
        tut.plot_convex_hull(points, convex_hull, "Quick Hull")


points = tut.random_collinear(80, 0, 1000, 0, True)

test_correctness_graham_scan(points)
test_correctness_jarvis(points)
test_correctness_divide_and_conquer(points)
test_correctness_quick_hull(points)
