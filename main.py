# This is a sample Python script.
import unittest
from FigureType import FigureType
from Vertice import Vertice
from quadrilateral import print_array
import matplotlib.pyplot as plt

def generate_parallelogram_points(width, height):
    return [Vertice(0, 0), Vertice(width, 0), Vertice(width + height, height), Vertice(height, height)]


def generate_rectangle_points(width, height):
    return [Vertice(0, 0), Vertice(width, 0), Vertice(width, height), Vertice(0, height)]


def generate_square_points(side_length):
    return [Vertice(0, 0), Vertice(side_length, 0), Vertice(side_length, side_length), Vertice(0, side_length)]


def generate_trapezoid_points(base1, base2, height):
    return [Vertice(0, 0), Vertice(base1, 0), Vertice(base2 + height, height), Vertice(height, height)]


def generate_isosceles_trapezoid_points(base_width, top_width, height):
    half_base = base_width / 2.0
    half_top = top_width / 2.0

    # Define the vertices of the trapezoid
    vertices = [Vertice(-half_base,0), Vertice(half_base,0), Vertice(half_top,height), Vertice(-half_top,height)]
    return vertices


def generate_rectangular_trapezoid_points(base1, base2, height):
    return [Vertice(0, 0), Vertice(base1, 0), Vertice(base2, height), Vertice(0, height)]


def generate_diamond_points(diagonal1, diagonal2):
    return [Vertice(0, diagonal1 / 2), Vertice(diagonal2 / 2, 0), Vertice(0, -diagonal1 / 2),
            Vertice(-diagonal2 / 2, 0)]

import unittest
import diamond
import Square
import isocle_trapezoid
import Trapezoid
import parallelogram
import rectangle
import rect_trapezoid


class TestQuadrilateral(unittest.TestCase):
    def test_parallelogram(self):
        points = generate_parallelogram_points(5, 3)

        quadrilateral = parallelogram.Parallelogram(points)
        self.assertEqual(quadrilateral.get_perimeter(), 18.485281374238568)
        self.assertEqual(quadrilateral.get_area(), 14.999999999999998)
        self.assertTrue(quadrilateral.is_shape_type(FigureType.Parallelogram))
        self.assertTrue(quadrilateral.check_main_properties())

    def test_rectangle(self):
        points = generate_rectangle_points(5, 3)
        quadrilateral = rectangle.Rectangle(points)
        self.assertEqual(quadrilateral.get_perimeter(), 16)
        self.assertEqual(quadrilateral.get_area(), 15)
        self.assertTrue(quadrilateral.is_shape_type(FigureType.Rectangle))
        self.assertTrue(quadrilateral.check_main_properties())


    def test_square(self):
        points = generate_square_points(3)
        quadrilateral = Square.Square(points)
        self.assertEqual(quadrilateral.get_perimeter(), 12)
        self.assertEqual(quadrilateral.get_area(), 9)
        self.assertTrue(quadrilateral.is_shape_type(FigureType.Square))
        self.assertTrue(quadrilateral.check_main_properties())

    def test_trapezoid(self):
        points = generate_trapezoid_points(6,3,4)
        quadrilateral = Trapezoid.Trapezoid(points)
        self.assertEqual(quadrilateral.get_perimeter(), 18.77995987511004)
        self.assertEqual(quadrilateral.get_area(), 18.0)
        self.assertTrue(quadrilateral.is_shape_type(FigureType.Trapezoid))
        self.assertTrue(quadrilateral.check_main_properties())

    def test_isocles_trapezoid(self):
        points = generate_isosceles_trapezoid_points(6, 3, 2)
        quadrilateral = isocle_trapezoid.IsoclesTrapezoids(points)
        self.assertEqual(quadrilateral.get_perimeter(), 14.0)
        self.assertEqual(quadrilateral.get_area(), 9)
        self.assertTrue(quadrilateral.is_shape_type(FigureType.IsocleTrapezoid))
        self.assertTrue(quadrilateral.check_main_properties())
    def test_rect_trapezoid(self):
        points = generate_rectangular_trapezoid_points(6, 3, 4)
        quadrilateral = rect_trapezoid.RectTrapezoid(points)
        self.assertEqual(quadrilateral.get_perimeter(), 18)
        self.assertEqual(quadrilateral.get_area(),18.0)
        self.assertTrue(quadrilateral.is_shape_type(FigureType.RectTrapezoid))
        self.assertTrue(quadrilateral.check_main_properties())

    def test_diamond(self):
        points = generate_diamond_points(5,6)
        quadrilateral = diamond.Diamond(points)

        self.assertEqual(quadrilateral.get_perimeter(), 15.620499351813308)
        self.assertEqual(quadrilateral.get_area(), 14.999999999999998)
        self.assertTrue(quadrilateral.is_shape_type(FigureType.Diamond))
        self.assertTrue(quadrilateral.check_main_properties())
    def test_intersection(self):
        trapezoid_points = generate_trapezoid_points(6, 3, 4)

        trapezoid = Trapezoid.Trapezoid(trapezoid_points)
        rectangle_points2 = [Vertice(-5, -5), Vertice(-3, -5), Vertice(-3, -3), Vertice(-5, -3)]
        rectangle2 = rectangle.Rectangle(rectangle_points2)
        print(rectangle2.check_main_properties())
        diamond_points = generate_diamond_points(5, 6)
        d = diamond.Diamond(diamond_points)
        parallelogram_points = generate_parallelogram_points(5, 3)
        rectangle_points = generate_rectangle_points(5, 3)

        rect = rectangle.Rectangle(rectangle_points)
        p = parallelogram.Parallelogram(parallelogram_points)
        self.assertTrue(rect.check_intersection(trapezoid))
        self.assertTrue(p.check_intersection(d))
        self.assertFalse(p.check_intersection(rectangle2))

# Used for test
def test(quadrilateral):
    print(f"Type of shape: {quadrilateral.shape_type}")
    print(f"Vertices: {quadrilateral.vertices}")
    print(f"Side lengths: {quadrilateral.get_side_lengths()}")
    print(f"Perimeter: {quadrilateral.get_perimeter()}")
    print(f"Area: {quadrilateral.get_area()}")
    print(f"Diagonals lengths: {quadrilateral.get_diagonals_lengths()}")
    print(f"Angles: {quadrilateral.get_angles()}")
    is_parallelogram = quadrilateral.is_shape_type(FigureType.Parallelogram)
    is_rectangle = quadrilateral.is_shape_type(FigureType.Rectangle)
    is_diamond = quadrilateral.is_shape_type(FigureType.Diamond)
    is_square = quadrilateral.is_shape_type(FigureType.Square)
    is_trapezoid = quadrilateral.is_shape_type(FigureType.Trapezoid)
    is_isocles_trapezoid = quadrilateral.is_shape_type(FigureType.IsocleTrapezoid)
    is_rect_trapezoid = quadrilateral.is_shape_type(FigureType.RectTrapezoid)
    print(f"Is parallelogram: {is_parallelogram}")
    print(f"Is rectangle: {is_rectangle}")
    print(f"Is square: {is_square}")
    print(f"Is diamond: {is_diamond}")
    print(f"Is trapezoid: {is_trapezoid}")
    print(f"Is isocle trapezoid: {is_isocles_trapezoid}")
    print(f"Is rectangular trapezoid: {is_rect_trapezoid}")
    print(f"Check main properties: {quadrilateral.check_main_properties()}")


if __name__ == '__main__':
    unittest.main()
