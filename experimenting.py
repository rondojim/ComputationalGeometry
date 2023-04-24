import convex_hull_algos.graham_scan as gs
import convex_hull_algos.jarvis as jr
import convex_hull_algos.divide_and_conquer as dc
import convex_hull_algos.quick_hull as qh
import math
import time
import matplotlib.pyplot as plt
from tqdm import tqdm

import utilities.geometry_utils as geom
import utilities.testing_utils as tut


# we will test the algorithms on 20 tests cases
# 10 of them will be random
# 10 of them will have many collinear points

results = {}
algorithms = [
    ("Graham Scan", gs.Graham_scan),
    ("Jarvis", jr.Jarvis),
    ("Divide and Conquer", dc.DC_convex_hull),
    ("Quick Hull", qh.Quick_hull),
]

for val in algorithms:
    results[val[0]] = {}

num_cases = 8

for t in tqdm(range(num_cases)):
    p1 = int(math.ceil((t + 1) / 2.0)) + 2
    # p2 = int(math.ceil(p1 / 2.0)) + 1
    points = []
    points_no_same_x = []

    type_ = "a"
    if t % 2 == 0:
        points = tut.random_point_set(10**p1, 0, 10**p1, False)
        points_no_same_x = tut.random_point_set(10**p1, 0, 10**p1, True)
    else:
        points = tut.random_collinear(10**p1, 0, 10**p1, 0, False)
        points_no_same_x = tut.random_collinear(10**p1, 0, 10**p1, 0, True)
        type_ = "b"

    for tup in algorithms:
        algo = tup[0]
        func = tup[1]

        cur_points = points
        if algo == "Divide and Conquer":
            cur_points = points_no_same_x

        start_time = time.time()
        output = func(cur_points)
        end_time = time.time()

        elapsed_time = end_time - start_time
        is_correct = geom.check_convex_hull(output, cur_points)
        results[algo][f"Test Case {p1 - 2}{type_}"] = {
            "time": elapsed_time,
            "is_correct": is_correct,
        }

table = [
    [" "]
    + [
        f"Test Case {int(math.ceil((i + 1) / 2.0))}{'a' if i % 2 == 0 else 'b'}\n$10^{math.ceil((i + 1) / 2.0) + 2}$ points\n{'random' if i % 2 == 0 else 'collinear'}"
        for i in range(num_cases)
    ]
]

for algorithm_name, result in results.items():
    print(f"{algorithm_name} with results: {result}\n")
    row = [algorithm_name]
    for i in range(num_cases):
        cell = result[
            f"Test Case {int(math.ceil((i + 1) / 2.0))}{'a' if i % 2 == 0 else 'b'}"
        ]
        if cell["is_correct"]:
            row.append(f"{cell['time']:.2f}s \u2713")
        else:
            row.append(f"{cell['time']:.2f}s \u2717")
    table.append(row)

# Plot the table as an image
fig, ax = plt.subplots()
ax.axis("off")
ax.axis("tight")
table = ax.table(cellText=table, loc="center")
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.2, 2)

for i in range(4):
    cell = table.get_celld()[(i + 1, 0)]
    text = cell.get_text()
    text.set_fontweight("bold")

for i in range(num_cases):
    cell = table.get_celld()[(0, i + 1)]
    text = cell.get_text()
    text.set_color("blue")

for i in range(4):
    for j in range(num_cases):
        p1 = int(math.ceil((j + 1) / 2.0)) + 2
        type_ = "a" if j % 2 == 0 else "b"
        cell = table.get_celld()[(i + 1, j + 1)]
        if results[algorithms[i][0]][f"Test Case {p1 - 2}{type_}"]["is_correct"]:
            cell.set_facecolor((0.5, 1, 0.5, 0.5))
        else:
            cell.set_facecolor((1, 0.5, 0.5, 0.5))

plt.show()
