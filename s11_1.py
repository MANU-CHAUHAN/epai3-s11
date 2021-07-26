import math


class MyPolygon:
    """A Polygon class"""

    def __init__(self, vertx_count, radius):
        """__init__ to initialize the radius and count during object creation"""

        if not isinstance(radius, int):
            raise TypeError("Seriously 😒!! Radius must be of integer type!")
        if radius < 0:
            raise ValueError("Woaahhh! Radius MUST be greater than 0! 👊")

        if not isinstance(vertx_count, int):
            raise TypeError("dude! you are supposed to pass vertex count as an `int` 😑")
        if vertx_count < 3:
            raise ValueError("Make sure you are passing AT LEAST 3 vertices, otherwise no need to use this class 😒")

        self._radius = radius
        self._vertx_count = vertx_count
        self._edge_length = None
        self._perimeter = None
        self._interior_angle = None
        self._apothem = None
        self._area = None

    @property
    def vertx_count(self):
        """property : getter: to get the count of vertices"""
        return self._vertx_count

    @property
    def radius(self):
        """Get radius"""
        return self._radius

    @property
    def edge_length(self):
        """Get property: edge length"""
        if self._edge_length is None:
            self._edge_length = 2 * self._radius * math.sin(math.pi / self._vertx_count)
        return self._edge_length

    @property
    def perimeter(self):
        """Get property: total perimeter"""
        if self._perimeter is None:
            self._perimeter = self._vertx_count * self.edge_length
        return self._perimeter

    @property
    def interior_angle(self):
        """Get property: interior angle"""
        if self._interior_angle is None:
            self._interior_angle = ((self._vertx_count - 2) * 180) / math.pi
        return self._interior_angle

    @property
    def apothem(self):
        """Get property: apothem"""
        if self._apothem is None:
            self._apothem = self._radius * math.cos(math.pi / self._vertx_count)
        return self._apothem

    @property
    def area(self):
        """Get property: total area"""
        if self._area is None:
            self._area = 1 / 2 * (self._vertx_count * self.edge_length * self.apothem)
        return self._area

    @property
    def edge_count(self):
        """Get edge count"""
        return self._vertx_count

    def __eq__(self, other):
        """ Check for the equality of MyPolygon"""
        if isinstance(other, MyPolygon):
            return self._vertx_count == other._vertx_count and self._radius == other.radius
        raise NotImplementedError("Comparison with other object type is not supported")

    def __gt__(self, other):
        """ Check for > MyPolygon"""
        if isinstance(other, MyPolygon):
            return self._vertx_count > other._vertx_count
        raise NotImplementedError("Comparison with other object type is not supported")

    def __ne__(self, other):
        """ Check for != MyPolygon"""
        return not self.__eq__(other)

    def __lt__(self, other):
        """ Check for < MyPolygon"""
        if isinstance(other, MyPolygon):
            return self._vertx_count < other._vertx_count
        raise NotImplementedError("Comparison with other object type is not supported")

    def __repr__(self):
        """ repr for MyPolygon"""
        return f"(MyPolygon({self._vertx_count}, {self._radius}))"


p = MyPolygon(12, 3)
print(p.area)
print(p.apothem)
print(p.edge_count)
print(p.edge_length)
print(p.interior_angle)
print(p.perimeter)
