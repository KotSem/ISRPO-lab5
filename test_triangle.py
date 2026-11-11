import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 5)
        self.assertAlmostEqual(res, 0.0)

    def test_normal_area(self):
        res = area(6, 4)
        self.assertAlmostEqual(res, 12.0)

    def test_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_float(self):
        res = perimeter(2.5, 3.5, 4.0)
        self.assertAlmostEqual(res, 10.0)


if __name__ == '__main__':
    unittest.main()
