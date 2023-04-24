import convex_hull_algos.graham_scan as gs
import convex_hull_algos.jarvis as jr
import convex_hull_algos.divide_and_conquer as dc
import convex_hull_algos.quick_hull as qh

import utilities.geometry_utils as geom
import utilities.testing_utils as tut


def test_correctness_graham_scan():
    points = tut.random_collinear(80, 0, 1000, 0, False)
    convex_hull = gs.Graham_scan(points)

    if geom.check_convex_hull(convex_hull, geom.convex_hull_brute(points)) == False:
        print("Graham Scan error")
    else:
        tut.plot_convex_hull(points, convex_hull, "Graham Scan")


def test_correctness_jarvis():
    points = tut.random_collinear(80, 0, 1000, 0, False)
    convex_hull = jr.Jarvis(points)

    if geom.check_convex_hull(convex_hull, geom.convex_hull_brute(points)) == False:
        print("Jarvis error")
    else:
        tut.plot_convex_hull(points, convex_hull, "Jarvis")


def test_correctness_divide_and_conquer():
    points = tut.random_collinear(80, 0, 1000, 0, True)
    convex_hull = dc.DC_convex_hull(points)

    if geom.check_convex_hull(convex_hull, geom.convex_hull_brute(points)) == False:
        print("Divide and Conquer error")
    else:
        tut.plot_convex_hull(points, convex_hull, "Divide and Conquer")


def test_correctness_quick_hull():
    points = tut.random_collinear(80, 0, 1000, 0, False)
    convex_hull = qh.Quick_hull(points)
    if geom.check_convex_hull(convex_hull, geom.convex_hull_brute(points)) == False:
        print("Quick hull error")
    else:
        tut.plot_convex_hull(points, convex_hull, "Quick Hull")


test_correctness_graham_scan()
test_correctness_jarvis()
test_correctness_divide_and_conquer()
test_correctness_quick_hull()
