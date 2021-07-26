import s11_1 as Polygon


class Polygons:
    """A `Polygon` Sequence class"""
    def __init__(self, m, R):
        if m < 3:
            raise ValueError("`m` must be greater than 3")
        self._m = m
        self._R = R
        self._polygons = [Polygon.MyPolygon(vertx_count=i, radius=R) for i in range(3, m + 1)]

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'

    def __getitem__(self, s):
        return self._polygons[s]

    def __iter__(self):
        return self.PolygonIterator(self)

    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons,
                                 key=lambda p: p.area / p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]

    class PolygonIterator:
        def __init__(self, poly_obj) -> None:
            self.index = 0
            self._poly_obj = poly_obj

        def __next__(self):
            if self.index >= len(self._poly_obj):
                raise StopIteration
            item = self._poly_obj._polygons[self.index]
            self.index += 1
            return item

        def __iter__(self):
            return self
