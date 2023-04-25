# **Computational Geometry: Part A**

## Introduction
<p align="justify">
Implementing algorithms in Python from scratch for computing convex hull of points. Every algorithm is tested extensively in different inputs including edge cases. The correcteness of the implementation of each algorithm is checked by comparing the results with the ones of the brute-force sub-optimal solution. Moreover, the user can execute each algorithm and examine the results from the plot of the convex hull, along with the rest of the points, that is created. For the Divide and Conquere algorithm is also provided a script for creating step-by-step visuals for a test case provided. The rest of the visuals for the other algorithms presented below are extracted from Wikipedia. Lastly, all algorithms are tested under the same cases and a comparison table of their performance is provided.
</p>

## Alorithms

- Graham scan
  <p align="justify">
  We set as the origin the leftmost lowest point and sort the rest of the points in increasing slope. Points with the same slope are sorted in increasing distance from the origin.
  
  We process the points in this order and we try to add each one in the convex hull. While the current point is more counter clockwise from the last point in convex hull in respect to the second to last point in convex hull, we remove the last one.
  
  Time complexity: $O(nlogn)$
  
  </p>

  ![Demo Gif](https://github.com/rondojim/ComputationalGeometry/blob/main/visuals/gifs/GrahamScanDemo.gif)

- Jarvis (Gift wrapping)
  <p align="justify">
    We start with the most left point and add it to convex hull and loop through the rest of the points in order to find the next point on the convex hull. We make sure to select a point that forms a line with the previous convex hull point which has the rest of the points on the same side. We find such a point by checking orientations or by comparing polar angles.

    Time complexity: $O(nh)$, where $h$ is the number of points on the convex hull
  </p>

  ![Demo gif](https://github.com/rondojim/ComputationalGeometry/blob/main/visuals/gifs/JarvisDemo.gif)
  
 - Divide and Conquer
   <p align="justify">
     We divide the points in two subsets with approximately equal sizes. We find recursively the convex hull for each subset and then merge the solutions.
     
     In order to merge the two convex hulls we compute the upper and lower tangents of the two convex polygon that were formed. Then the points that are "inside", between the two tangents, are discarded.
     
     Time complexity: $O(nlogn)$
  </p>
  
  ![Demo gif](https://github.com/rondojim/ComputationalGeometry/blob/main/visuals/gifs/DivideAndConquerDemo.gif)
  
- Quick Hull
   <p align="justify">
   We find the leftmost point $A$ and rightmost point $B$. We add $A$ and $B$ to convex hull. We create two sets $S_1$ and $S_2$ with the points on the left and right side of segment $AB$ respectively. We find convex hull on $S_1$ and on $S_2$ and add the points to the total convex hull.
   
   In order to find the convex hull in each set we find the point $C$ with the maximum distance from the line. All the points inside triangle $ABC$ will not be part of the convex hull. Then we again create two sets for points on the left and right side of the triangle and solve recursively.
  
    Time complexity: Best case $O(nlogn)$ Worst case $O(n^{2})$
  </p>
  
  ![Demo gif](https://github.com/rondojim/ComputationalGeometry/blob/main/visuals/gifs/Animation_depicting_the_quickhull_algorithm.gif)

## Testing

<p align = "justify">
Every algorithm is tested on 8 different test cases. Four of them are created randomly and we just ensure that no point appears in the point set more than once. The rest of them are created using the same procedure except that for every point we insert in the point set, there is a high probability that we will add two more points that will be collinear in respect to this point. Moreover, note that the divide and conquer algorithm was tested with the same test cases as the other algorithms, where two points with same x-coordinate may were present. 

The point sets have sizes $10^{3}, 10^{4}, 10^{5}, 10^{6}$ and the output for each algorithm for each test cases is checked by ensuring that the resulting convex hull is really convex and that every other point is inside or on the convex hull.

We used a python script to gather all the results and form a table with our experiments. Every cell that is green means that the answer is correct. If it is red it means that the answer is wrong:
</p>

![Experiments](https://github.com/rondojim/ComputationalGeometry/blob/main/experiments/tables/experiments.png)

<p align = "justify">
Below we can see another table where we compare the algorithms again, but now all of the algorithms are tested on test cases where no two points with the same x-coordinates are present, in order to compare fairly the algorithms.
</p>

![Experiments](https://github.com/rondojim/ComputationalGeometry/blob/main/experiments/tables/experiments_2.png)

<p align = "justify">
We also present the plots created for each algorithm for the same test cases with 80 points and the list of the points that belong to the convex hull according to each algorithm.
</p>

- Graham Scan
  
  Convex hull: ```[(3, 651), (14, 351), (17, 331), (70, 181), (163, 61), (247, 20), (461, 17), (816, 15), (949, 30), (993, 114), (999, 985), (891, 991), (39, 963)]```
  
  ![Plot](https://github.com/rondojim/ComputationalGeometry/blob/main/visuals/imgs/graham_scan.png)
  
- Jarvis
  
  Convex hull: ```[(3, 651), (14, 351), (17, 331), (70, 181), (163, 61), (247, 20), (461, 17), (816, 15), (949, 30), (993, 114), (999, 985), (891, 991), (39, 963)]```
   
  ![Plot](https://github.com/rondojim/ComputationalGeometry/blob/main/visuals/imgs/jarvis.png)
  
- Divide and Conquer
  
  Convex hull: ```[(39, 963), (3, 651), (14, 351), (17, 331), (70, 181), (163, 61), (247, 20), (461, 17), (816, 15), (949, 30), (993, 114), (999, 985), (891, 991)]``` (${\color{red}Note \space here \space that \space the \space list \space is \space just \space shifted \space by \space one}$)
  
  ![Plot](https://github.com/rondojim/ComputationalGeometry/blob/main/visuals/imgs/divide_and_conquer.png)
  
- Quick Hull

  Convex hull: ```[(3, 651), (14, 351), (17, 331), (70, 181), (163, 61), (247, 20), (461, 17), (816, 15), (949, 30), (993, 114), (999, 985), (891, 991), (39, 963)]```
  
  ![Plot](https://github.com/rondojim/ComputationalGeometry/blob/main/visuals/imgs/quick_hull.png)
  

## 3D convex hull

<p align="justify">
  We use the ConvexHull function from scipy.spatial to compute the three dimensional convex hull of 50 points. This functions uses the Quick Hull algorithm. Below we can see the list of 50 random points in the three dimensional space. We also implemented a script for producing the plot for their convex hull.
</p>

Points: ```[(1, 69, 57), (4, 93, 45), (5, 69, 5), (7, 13, 42), (9, 60, 85), (9, 70, 21), (10, 46, 65), (17, 73, 17), (19, 42, 71), (20, 90, 74), (22, 56, 69), (23, 2, 9), (24, 87, 56), (28, 46, 46), (31, 65, 93), (32, 59, 3), (34, 17, 8), (39, 13, 51), (39, 61, 67), (39, 77, 52), (40, 26, 27), (42, 66, 39), (44, 8, 25), (44, 19, 76), (44, 56, 71), (45, 40, 77), (49, 37, 46), (50, 85, 1), (53, 24, 76), (53, 49, 2), (54, 82, 3), (56, 59, 98), (56, 80, 58), (57, 38, 66), (60, 54, 86), (62, 31, 67), (62, 100, 96), (65, 10, 73), (65, 67, 36), (66, 76, 81), (69, 49, 97), (69, 66, 100), (70, 68, 54), (71, 73, 6), (72, 89, 58), (78, 90, 61), (79, 19, 63), (83, 11, 26), (91, 81, 73), (94, 55, 46)]```

![Plot](https://github.com/rondojim/ComputationalGeometry/blob/main/visuals/gifs/3D_convex_hull.gif)


## Conclusion - 2D algorithms

<p align = "justify">
Regarding degenerate cases, Graham Scan, Jarvis (Gift Wrapping), and Quick Hull algorithms seem to behave correctly. They produce the correct output in both random cases (where collinear points might appear) and in cases where there are a lot of collinear points. On the other hand Divide and Conquer algorithm seems to enter an endless loop in cases where more than two points appear with the same x-coordinate, so we made sure to exit if the input has this property. Despite this, Divide and Conquer produces correct output in all other cases.
</p>
