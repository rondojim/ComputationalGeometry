import sys

sys.path.append("../utilities")
sys.path.append("../../PartA/utilities")

import kdtree as kd
import testing_utils as tu
import random
import brute_force_checker as bfc
import pandas as pd
import matplotlib.pyplot as plt

verdict = []

for N in range(1000, 10001, 1000):
    points = tu.random_point_set(N, 1, 200, False)
    tree = kd.kdtree(points, 2)
    minx = random.randint(1, 100)
    maxx = random.randint(minx + 1, 200)
    miny = random.randint(1, 100)
    maxy = random.randint(miny + 1, 200)
    in_rectangle = tree.search_rectangle(minx, maxx, miny, maxy)
    verdict.append(
        bfc.check_kd_tree_result(points, in_rectangle, minx, maxx, miny, maxy)
    )
print(verdict)
