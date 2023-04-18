# **Computational Geometry: Part A**

## Introduction
<p align="justify">
Implementing algorithms in Python from scratch for computing convex hull of points. Every algorithm is tested extensively in different inputs including edge cases. The correcteness of the implementation of each algorithm is checked by comparing the results with the ones of the brute-force sub-optimal solution. Moreover, the user can execute each algorithm and examine the results from the plot of the convex hull, along with the rest of the points, that is created. For "Graham Scan's" algorithm is also provided a script for creating step-by-step visuals for a test case provided. The visuals presented below are extracted from Wikipedia. Lastly, all algorithms are tested under the same cases and a comparison table of their performance is provided.
</p>

## Alorithms

- Graham scan
  <p align="justify">
  We set as the origin the leftmost lowest point and sort the rest of the points in increasing slope. Points with the same slope are sorted in increasing distance from the origin.
  
  We process the points in this order and we try to add each one in the convex hull. While the current point is more counter clockwise from the last point in convex hull in respect to the second to last point in convex hull, we remove the last one.
  </p>

  ![Demo Gif](https://github.com/rondojim/ComputationalGeometry/blob/main/visuals/GrahamScanDemo.gif)

- Jarvis (Gift wrapping)

  <p align="justify">
  </p>

  ![Demo gif](https://github.com/rondojim/ComputationalGeometry/blob/main/visuals/JarvisDemo.gif)
