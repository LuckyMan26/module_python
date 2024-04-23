import math
from abc import ABC
from math import sin

from FigureType import FigureType
from Vertice import get_distance, angle_between_points
from quadrilateral import Quadrilateral


class Parallelogram(Quadrilateral):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.shape_type = FigureType.Parallelogram

        self.area = self.length[0] * self.length[1] * sin(math.radians(self.angles[0]))

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
        return [FigureType.Diamond, FigureType.Square, FigureType.Rectangle]

    @classmethod
    def get_shape_supertypes(cls):
        return [FigureType.Quadrilateral, FigureType.Parallelogram]

    def check_main_properties(self):
        eps = 0.0001
        if abs(self.length[0] - self.length[2])>eps or abs(self.length[1] - self.length[3])>eps:
            return False
        if abs(self.angles[0] - self.angles[2])>eps or abs(self.angles[1] - self.angles[3])>eps:
            return False
        return True
