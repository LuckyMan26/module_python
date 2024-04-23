from math import sqrt

from FigureType import FigureType
from Trapezoid import Trapezoid
from Vertice import get_distance, angle_between_points


class IsoclesTrapezoids(Trapezoid):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.shape_type = FigureType.IsocleTrapezoid
    def get_area(self):
        return self.area

    def get_angles(self):
        return self.angles

    def get_perimeter(self):
        return self.perimeter

    def get_side_lengths(self):
        return self.length

    def get_diagonals_lengths(self):
        return self.diagonals

    def get_vertex_coordinates(self):
        return self.vertices

    @classmethod
    def get_shape_subtypes(cls):
        return []

    @classmethod
    def get_shape_supertypes(cls):
        return [FigureType.Quadrilateral, FigureType.Trapezoid, FigureType.IsocleTrapezoid]



    def check_main_properties(self):
        eps = 0.00001
        if not super().check_main_properties():
            return False
        if abs(self.length[0] - self.length[2])<eps:
            return True
        return False
