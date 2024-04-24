# This is a sample Python script.
from FigureType import FigureType
from Square import Square
from Trapezoid import Trapezoid
from Vertice import Vertice
from diamond import Diamond
from parallelogram import Parallelogram
from quadrilateral import print_array
from rectangle import Rectangle
from isocle_trapezoid import IsoclesTrapezoids
from rect_trapezoid import RectTrapezoid


def generate_parallelogram_points(width, height):
    return [Vertice(0, 0), Vertice(width, 0), Vertice(width + height, height), Vertice(height, height)]


def generate_rectangle_points(width, height):
    return [Vertice(0, 0), Vertice(width, 0), Vertice(width, height), Vertice(0, height)]


def generate_square_points(side_length):
    return [Vertice(0, 0), Vertice(side_length, 0), Vertice(side_length, side_length), Vertice(0, side_length)]


def generate_trapezoid_points(base1, base2, height):
    return [Vertice(0, 0), Vertice(base1, 0), Vertice(base2 + height, height), Vertice(height, height)]


def generate_isosceles_trapezoid_points(base, height, leg):
    return [Vertice(0, 0), Vertice(base, 0), Vertice(base + (leg / 2), height), Vertice((leg / 2), height)]


def generate_rectangular_trapezoid_points(base1, base2, height):
    return [Vertice(0, 0), Vertice(base1, 0), Vertice(base2, height), Vertice(0, height)]


def generate_diamond_points(diagonal1, diagonal2):
    return [Vertice(0, diagonal1 / 2), Vertice(diagonal2 / 2, 0), Vertice(0, -diagonal1 / 2),
            Vertice(-diagonal2 / 2, 0)]


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
    #Тести, щоб перевірити коректність програми(юніт тести)
    parallelogram_points = generate_parallelogram_points(5, 3)
    print("Parallelogram points:")
    print_array(parallelogram_points)
    parallelogram = Parallelogram(parallelogram_points)
    test(parallelogram)
    rectangle_points = generate_rectangle_points(5, 3)
    print("\nRectangle points:")
    print_array(rectangle_points)
    rectangle = Rectangle(rectangle_points)
    test(rectangle)

    square_points = generate_square_points(4)
    print("\nSquare points:")
    print_array(square_points)
    square = Square(square_points)
    test(square)

    trapezoid_points = generate_trapezoid_points(6, 3, 4)
    print("\nTrapezoid points:")
    print_array(trapezoid_points)
    trapezoid = Trapezoid(trapezoid_points)
    test(trapezoid)

    isosceles_trapezoid_points = generate_isosceles_trapezoid_points(6, 4, 2)
    print("\nIsosceles Trapezoid points:")
    print_array(isosceles_trapezoid_points)
    isosceles_trapezoid = IsoclesTrapezoids(isosceles_trapezoid_points)
    test(isosceles_trapezoid)

    rectangular_trapezoid_points = generate_rectangular_trapezoid_points(6, 3, 4)
    print("\nRectangular Trapezoid points:")
    print_array(rectangular_trapezoid_points)
    rect_trapezoid = RectTrapezoid(rectangular_trapezoid_points)
    test(rect_trapezoid)

    diamond_points = generate_diamond_points(5, 6)
    print("\nDiamond points:")
    print_array(diamond_points)
    diamond = Diamond(diamond_points)
    test(diamond)
    rectangle_points2 = [Vertice(-5, -5), Vertice(-3, -5), Vertice(-3, -3), Vertice(-5, -3)]
    rectangle2 = Rectangle(rectangle_points2)
    print(rectangle2.check_main_properties())

    print(f"Check if intersects: {rectangle.check_intersection(trapezoid)}")
    print(f"Check if intersects: {parallelogram.check_intersection(diamond)}")
    print(f"Check if intersects: {parallelogram.check_intersection(rectangle2)}")