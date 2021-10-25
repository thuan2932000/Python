import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 3)

print(p.x)
print(p.y)

class LineSegment:
    def __init__(self, point1, point2):
        self.startpoint = point1
        self.endpoint = point2
    def slope(self):
        return (self.endpoint.y - self.startpoint.y) /(self.endpoint.x - self.startpoint.x)
    def length(self):
        return math.sqrt(
 (self.endpoint.x - self.startpoint.x)**2 +
 (self.endpoint.y - self.startpoint.y)**2)
segment = LineSegment(Point(1, 1), Point(3, 2))
print(segment.slope())

p1 = Point(1, 3)
p2 = Point(3, 2)
segment = LineSegment(p1, p2)
print (segment.startpoint == p1)
print (segment.endpoint == p2)
segment = LineSegment(Point(1, 1), Point(3, 2))
print(segment.slope())
print(segment.length())