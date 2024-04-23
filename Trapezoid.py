import math
from math import sqrt

from FigureType import FigureType
from Vertice import get_distance, angle_between_points
from quadrilateral import Quadrilateral


class Trapezoid(Quadrilateral):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.shape_type = FigureType.Trapezoid
        atitude = sqrt(self.length[0] ** 2 - ((self.length[3] - self.length[1]) / 2) ** 2)
        self.area = atitude * (self.length[0] + self.length[2]) / 2

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
        return [FigureType.RectTrapezoid, FigureType.IsocleTrapezoid]

    @classmethod
    def get_shape_supertypes(cls):
        return [FigureType.Quadrilateral, FigureType.Trapezoid]



    def check_main_properties(self):
        eps=0.00001
        if (not (abs(self.angles[0] + self.angles[1] - 180)>eps) and abs(self.angles[2] + self.angles[3] - 180)>eps) and (
                abs(self.angles[0] - self.angles[2])>eps):
            return False
        return True
