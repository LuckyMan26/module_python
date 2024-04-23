from math import sqrt, acos, degrees


class Vertice(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

def get_distance(vertice1, vertice2):
    dist = sqrt((vertice1.x-vertice2.x)**2+(vertice1.y-vertice2.y)**2)
    return dist

def angle_between_points(A, B, C):
    a = get_distance(B, C)
    b = get_distance(A, C)
    c = get_distance(A, B)

    angle_rad = acos((b**2 + c**2 - a**2) / (2 * b * c))
    angle_deg = degrees(angle_rad)

    return angle_deg

