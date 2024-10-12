from math import hypot

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)
        
    def getx(self):
        return self.__x
    def gety(self):
        return self.__y
    def distance_from_xy(self, x, y):
        return hypot(self.__x - x, self.__y - y)
    def distance_from_point(self, point):
        return hypot(self.__x - point.getx(), self.__y - point.gety())
    
class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__v1 = vertice1
        self.__v2 = vertice2
        self.__v3 = vertice3

    def perimeter(self):
        side1 = self.__v1.distance_from_point(self.__v2)
        side2 = self.__v2.distance_from_point(self.__v3)
        side3 = self.__v3.distance_from_point(self.__v1)
        return side1 + side2 + side3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
