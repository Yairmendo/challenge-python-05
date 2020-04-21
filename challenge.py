import math


def square_area(side):
    """Returns the area of a square"""
    return side**2
    


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    return base*height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    return (base*height)/2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    return (diagonal_1*diagonal_2)/2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    return ((base_minor+base_major)/2)*height


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    return (perimeter*apothem)/2


def circumference_area(radius):
    """Returns the area of a circumference"""
    return round(math.pi*(radius**2))



if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            # Initialize the needed values for the tests
            self.side = 5
            self.base = 5
            self.height = 2
            self.diagonal_1 = 10 
            self.diagonal_2 = 4
            self.base_minor = 2
            self.base_major = 6
            self.perimeter = 20
            self.apothem = 6
            self.radius = 6

            
        def test_square_area(self):
            square_answer = square_area(self.side)
            self.assertEqual(square_answer, 25)


        def test_rectangle_area(self):
            rectangle_answer = rectangle_area(self.base, self.height)
            self.assertEqual(rectangle_answer, 10)
            

        def test_triangle_area(self):
            triangle_answer = triangle_area(self.base, self.height)
            self.assertEqual(triangle_answer, 5)


        def test_rhombus_area(self):
            rhombus_answer = rhombus_area(self.diagonal_1, self.diagonal_2 )
            self.assertEqual(rhombus_answer, 20)


        def test_trapezoid_area(self):
            trapezoid_answer = trapezoid_area(self.base_minor, self.base_major, self.height)
            self.assertEqual(trapezoid_answer, 8)


        def test_regular_polygon_area(self):
            regular_polygon_answer = regular_polygon_area(self.perimeter, self.apothem)
            self.assertEqual(regular_polygon_answer, 60)


        def test_circumference_area(self):
            circumference_answer = circumference_area(self.radius)
            self.assertEqual(circumference_answer, 113)

        def tearDown(self):
        # Delete the needed values for the tests
            del(self.side)
            del(self.base)
            del(self.height)
            del(self.diagonal_1)
            del(self.diagonal_2)
            del(self.base_minor)
            del(self.base_major)
            del(self.perimeter)
            del(self.apothem)
            del(self.radius)


    unittest.main()




