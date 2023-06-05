class kdtree(object):
    def __init__(self, points, dimensions):
        def create_kdtree(points, dimension=0):
            if len(points) > 1:
                points.sort(key=lambda point: point[dimension])
                dimension = (dimension + 1) % dimensions
                median = len(points) >> 1
                return [
                    create_kdtree(points[:median], dimension),
                    create_kdtree(points[median + 1 :], dimension),
                    points[median],
                ]
            elif len(points) == 1:
                return [None, None, points[0]]

        def search_rectangle(node_, a, b, c, d):
            result = []

            def search_in_rectangle(node, a, b, c, d, dimension=0):
                if node:
                    point = node[2]
                    x, y = point[0], point[1]

                    if a <= x and x <= b and c <= y and y <= d:
                        result.append(point)

                    if x > a and node[0]:
                        search_in_rectangle(
                            node[0], a, b, c, d, (dimension + 1) % dimensions
                        )
                    if x < b and node[1]:
                        search_in_rectangle(
                            node[1], a, b, c, d, (dimension + 1) % dimensions
                        )

            search_in_rectangle(node_, a, b, c, d)
            return result

        self._root = create_kdtree(points)
        self._search_rectangle = search_rectangle

    def search_rectangle(self, a, b, c, d):
        return self._search_rectangle(self._root, a, b, c, d)
