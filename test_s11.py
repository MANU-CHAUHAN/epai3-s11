import math
import pytest
from s11_2 import Polygons
from s11_1 import MyPolygon


def test_polygon1():
    with pytest.raises(ValueError):
        MyPolygon(vertx_count=2, radius=10)


def test_polygon2():
    abs_tol = 1
    rel_tol = 0.001
    n = 3
    R = 1
    p = MyPolygon(vertx_count=n, radius=R)

    assert p.vertx_count == n, (f'actual: {p.vertx_count},'
                                f' expected: {n}')
    assert p.edge_count == n, f'actual: {p.edge_count}, expected: {n}'
    assert p.radius == R, f'actual: {p.radius}, expected: {n}'
    assert p.interior_angle == 57.29577951308232, (f'actual: {p.interior_angle},'
                                                   ' expected: 57.29577951308232')
    n = 4
    R = 1
    p = MyPolygon(vertx_count=n, radius=R)
    assert p.interior_angle == 114.59155902616465, (f'actual: {p.interior_angle}, '
                                                    ' expected: 114.59155902616465')
    assert math.isclose(p.area, 2,
                        rel_tol=abs_tol,
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')

    assert math.isclose(p.edge_length, math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.edge_length},'
                                           f' expected: {math.sqrt(2)}')

    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           f' expected: {4 * math.sqrt(2)}')

    assert math.isclose(p.apothem, 0.707,
                        rel_tol=rel_tol,
                        abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                           ' expected: 0.707')
    p = MyPolygon(6, 2)
    assert math.isclose(p.edge_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.interior_angle, 230,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    p = MyPolygon(12, 3)
    assert math.isclose(p.edge_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)

    p1 = MyPolygon(vertx_count=3, radius=10)
    p2 = MyPolygon(vertx_count=10, radius=10)
    p3 = MyPolygon(vertx_count=15, radius=10)
    p4 = MyPolygon(vertx_count=15, radius=100)
    p5 = MyPolygon(vertx_count=15, radius=100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5


def test_count_vertices():
    assert MyPolygon(4, 4).vertx_count == 4, 'vertx_count: no match'


def test_count_edges():
    assert MyPolygon(4, 4).edge_count == 4, 'edge_count: no match'


def test_polygons_len():
    assert Polygons(7, 10).__len__() == 5, 'length: no match'


def test_radius():
    assert MyPolygon(4, 4).radius == 4, 'radius: no match'


def test_interior_angle():
    assert MyPolygon(3, 1).interior_angle == 57.29577951308232, 'interior_angle: no match'


def test_edge_length():
    assert MyPolygon(7, 10).edge_length == 8.677674782351163, 'edge_length: no match'


def test_apothem():
    assert MyPolygon(7, 10).apothem == 9.009688679024192, 'apothem: no match'


def test_area():
    assert MyPolygon(7, 10).area == 273.6410188638105, 'area: no match'


def test_perimeter():
    assert MyPolygon(7, 10).perimeter == 60.74372347645814, 'perimeter: no match'


def test_exhaustion():
    polygons = iter(Polygons(5, 5))
    for poly in polygons:
        pass
    with pytest.raises(StopIteration):
        next(polygons)


def test_iteration():
    polygons = Polygons(5, 10)
    iter_poly = iter(polygons)
    assert str(next(iter_poly)) == '(MyPolygon(3, 10))', "Check the implementation"
    next(iter_poly)
    next(iter_poly)
    with pytest.raises(StopIteration):
        next(iter_poly)


def test_iterator():
    polygons = Polygons(10, 10)
    assert hasattr(polygons.PolygonIterator, '__iter__'), "Check the implementation"
    assert hasattr(polygons.PolygonIterator, '__next__'), "Check the implementation"
    assert hasattr(polygons, '__getitem__'), "Check the implementation"


def test_dir():
    polygons = Polygons(10, 10)
    iter_poly = iter(polygons)
    assert "__iter__" in dir(iter_poly), "Check the implementation"
    assert iter_poly.__next__(), "Check the implementation"
