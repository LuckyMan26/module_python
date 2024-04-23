from abc import ABC, abstractmethod

from Vertice import angle_between_points, get_distance
def print_array(array):
    for element in array:
        print(element)

def point_inside(point, vertices):
    intersect_count = 0
    for i in range(len(vertices)):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % len(vertices)]
        if (p1.y > point.y) != (p2.y > point.y) and \
                point.x < (p2.x - p1.x) * (point.y - p1.y) / (p2.y - p1.y) + p1.x:
            intersect_count += 1
    res = intersect_count % 2 == 1
    return res


def segments_intersect(p1, p2, p3, p4):
    """
    Check if two line segments intersect.
    """

    def orientation(p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    o1 = orientation(p1, p2, p3)
    o2 = orientation(p1, p2, p4)
    o3 = orientation(p3, p4, p1)
    o4 = orientation(p3, p4, p2)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p3, p2):
        return True
    if o2 == 0 and on_segment(p1, p4, p2):
        return True
    if o3 == 0 and on_segment(p3, p1, p4):
        return True
    if o4 == 0 and on_segment(p3, p2, p4):
        return True
    return False


def on_segment(p, q, r):
    if (max(p.x, r.x) >= q.x >= min(p.x, r.x) and
            max(p.y, r.y) >= q.y >= min(p.y, r.y)):
        return True
    return False


class Quadrilateral(ABC):
    def __init__(self, vertices):

        self.vertices = vertices
        self.length = [
            get_distance(vertices[0], vertices[1]),
            get_distance(vertices[1], vertices[2]),
            get_distance(vertices[2], vertices[3]),
            get_distance(vertices[3], vertices[0])
        ]
        self.angles = [
            angle_between_points(vertices[0], vertices[1], vertices[3]),
            angle_between_points(vertices[1], vertices[2], vertices[0]),
            angle_between_points(vertices[2], vertices[1], vertices[3]),
            angle_between_points(vertices[3], vertices[0], vertices[2])
        ]
        self.perimeter = sum(self.length)
        self.diagonals = [
            get_distance(self.vertices[0], self.vertices[2]),
            get_distance(self.vertices[1], self.vertices[3])
        ]

    @abstractmethod
    def get_vertex_coordinates(self):
        pass

    @abstractmethod
    def get_side_lengths(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_diagonals_lengths(self):
        pass

    @abstractmethod
    def get_angles(self):
        pass

    @abstractmethod
    def check_main_properties(self):
        pass

    @classmethod
    @abstractmethod
    def get_shape_subtypes(cls):
        pass

    @classmethod
    def get_shape_supertypes(cls):
        return ['Quadrilateral']

    @classmethod
    def is_shape_type(cls, shape_type):
        return shape_type in cls.get_shape_supertypes()

    def compare_area(self, other_figure):
        """
               Compare the area of this figure with another figure.
               Returns:
                   -1 if this figure has smaller area,
                    0 if both figures have equal area,
                    1 if this figure has larger area.
               """
        if self.calculate_area() < other_figure.calculate_area():
            return -1
        elif self.calculate_area() > other_figure.calculate_area():
            return 1
        else:
            return 0

    def compare_perimeter(self, other_figure):
        """
               Compare the perimeter of this figure with another figure.
               Returns:
                   -1 if this figure has smaller perimeter,
                    0 if both figures have equal perimeter,
                    1 if this figure has larger perimeter.
               """
        if self.calculate_perimeter() < other_figure.calculate_perimeter():
            return -1
        elif self.calculate_perimeter() > other_figure.calculate_perimeter():
            return 1
        else:
            return 0

    def compare_area_and_perimeter(self, other_figure):
        """
        Compare the area and perimeter of this figure with another figure.
        Returns a tuple of comparison results:
            (-1, -1) if this figure has smaller area and perimeter,
            (-1, 0) if this figure has smaller area but equal perimeter,
            (-1, 1) if this figure has smaller area but larger perimeter,
            (0, -1) if both figures have equal area but smaller perimeter,
            (0, 0) if both figures have equal area and perimeter,
            (0, 1) if both figures have equal area but larger perimeter,
            (1, -1) if this figure has larger area but smaller perimeter,
            (1, 0) if this figure has larger area but equal perimeter,
            (1, 1) if this figure has larger area and perimeter.
        """
        area_comparison = self.compare_area(other_figure)
        perimeter_comparison = self.compare_perimeter(other_figure)

        return area_comparison, perimeter_comparison

    def check_intersection(self, other_figure):
        """
        Check if this figure intersects with another figure.
        Returns True if they intersect, False otherwise.
        """
        # Check if any vertex of one figure is inside the other figure
        for vertex in self.vertices:
            if point_inside(vertex, other_figure.vertices):
                return True
        for vertex in other_figure.vertices:
            if point_inside(vertex, self.vertices):
                return True

        # Check if any edge of one figure intersects with any edge of the other figure
        for i in range(len(self.vertices)):
            for j in range(len(other_figure.vertices)):
                if self.segments_intersect(self.vertices[i], self.vertices[(i + 1) % len(self.vertices)],
                                           other_figure.vertices[j],
                                           other_figure.vertices[(j + 1) % len(other_figure.vertices)]):
                    return True

        return False
