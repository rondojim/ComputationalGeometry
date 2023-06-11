class kdtree(object):
    def __init__(self, points, dimensions):
        def create_kdtree(points, dimension=0):
            """Recursive function to create a kd-tree from a list of points

            Args:
                points (list): The list of points to build the kd-tree from.
                dimension (int, optional): The current dimension to split the points. Defaults to 0.

            Returns:
                list: The constructed kd-tree as a nested list.
            """
            if len(points) > 1:
                points.sort(
                    key=lambda point: point[dimension]
                )  # Sort the points based on the current dimension
                dimension = (
                    dimension + 1
                ) % dimensions  # Update the dimension for the next level of recursion
                median = len(points) >> 1  # Find the median index of the sorted points
                return [
                    create_kdtree(
                        points[:median], dimension
                    ),  # Recursive call for the left subtree
                    create_kdtree(
                        points[median + 1 :], dimension
                    ),  # Recursive call for the right subtree
                    points[median],  # Median point as the current node
                ]
            elif len(points) == 1:
                return [None, None, points[0]]  # Leaf node containing a single point

        def search_rectangle(node_, a, b, c, d):
            """Recursive function to search for points within a given rectangle.

            Args:
                node_ (list): The current node of the kd-tree.
                a (float): The minimum x-coordinate of the rectangle.
                b (float): The maximum x-coordinate of the rectangle.
                c (float): The minimum y-coordinate of the rectangle.
                d (float): The maximum y-coordinate of the rectangle.

            Returns:
                list: The list of points within the rectangle.
            """
            result = []

            def search_in_rectangle(node, a, b, c, d, dimension=0):
                if node:
                    point = node[2]  # Get the point stored in the current node
                    x, y = point[0], point[1]

                    if a <= x and x <= b and c <= y and y <= d:
                        result.append(
                            point
                        )  # Add the point to the result if it falls within the rectangle

                    if dimension == 0:
                        if x >= a and node[0]:
                            # Recursively search the left subtree if it potentially intersects with the rectangles
                            search_in_rectangle(
                                node[0], a, b, c, d, (dimension + 1) % dimensions
                            )
                        if x <= b and node[1]:
                            # Recursively search the right subtree if it potentially intersects with the rectangles
                            search_in_rectangle(
                                node[1], a, b, c, d, (dimension + 1) % dimensions
                            )
                    else:
                        if y >= c and node[0]:
                            # Recursively search the left subtree if it potentially intersects with the rectangles
                            search_in_rectangle(
                                node[0], a, b, c, d, (dimension + 1) % dimensions
                            )
                        if y <= d and node[1]:
                            # Recursively search the right subtree if it potentially intersects with the rectangles
                            search_in_rectangle(
                                node[1], a, b, c, d, (dimension + 1) % dimensions
                            )

            search_in_rectangle(node_, a, b, c, d)
            return result  # Return the list of points found within the rectangle

        self._root = create_kdtree(points)
        self._search_rectangle = search_rectangle

    def search_rectangle(self, a, b, c, d):
        return self._search_rectangle(self._root, a, b, c, d)
