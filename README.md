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

Every algorithm is tested on 8 different test cases. Four of them are created randomly and we just ensure that no point appears in the point set more than once. The rest of them are created using the same procedure except that for every point we insert in the point set, there is a probability that we will add two more points that will be collinear in respect to this point. Moreover, note that the divide and conquer algorithm was not tested with the same test cases as the other algorithms, but with ones where there are not two points with same x-coordinate present. 

The point sets have sizes $10^{3}, 10^{4}, 10^{5}, 10^{6}$ and the output for each algorithm for each test cases is checked by ensuring that the resulting convex hull is really convex and that every other point is inside or on the convex hull.

We used a python script to gather all the results and form a table with our experiments. Every cell that is green means that the answer is correct. If it is red it means that the answer is wrong:

![Experiments](https://github.com/rondojim/ComputationalGeometry/blob/main/experiments/tables/experiments.png)


Below we can see another table where we compare the algorithms again, but now the rest of the algorithms are tested on Divide and Conquer's test cases where no two points with the same x-coordinates are present.

![Experiments](https://github.com/rondojim/ComputationalGeometry/blob/main/experiments/tables/experiments_2.png)

