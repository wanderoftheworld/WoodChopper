import unittest
import random
from math import sin, cos, pi
from typing import Tuple

def randPoint(self, radius: float, center: Tuple[float, float]) -> Tuple[float, float]:
    """
    Returns a random point (uniform distribution) within the given circle.

    Args:
        radius: a float representing the radius of a circle 
        center: a tuple of two floats, representing center of the circle

    Returns:
        Tuple(float, float): coordinates for a random point within the circle

    Note:
    - This function raise ValueError if `radius` is 0 or negative
    """
    if radius <= 0:
        raise ValueError('Radius must be a positive number')

    randRadius = random.random() * radius
    randRadian = random.uniform(0, 2 * pi)
    x, y = center
    return (x + randRadius * sin(randRadian), y + randRadius * cos(randRadian))

class TestRandPoint(unittest.TestCase):
    expected_points = [(-0.10996222555283103, 0.07721437073087666),
        (0.7633872656914338, -0.02432182503489773),
        (0.15460380626465442, -0.470694793481169)]

    def test_good_input(self):
        random.seed(1)
        for i in range(len(self.expected_points)):
            self.assertEqual(self.expected_points[i], randPoint(1, (0, 0)))

    def test_radius_change(self):
        random.seed(1)
        radius = 0.5
        for i in range(len(self.expected_points)):
            x, y = self.expected_points[i]
            self.assertEqual((x * radius, y * radius), randPoint(radius, (0, 0)))
    
    def test_center_change(self):
        random.seed(1)
        cx, cy = 1, 2
        for i in range(len(self.expected_points)):
            x, y = self.expected_points[i]
            self.assertEqual(((x + cx), (y + cy)), randPoint(1.0, (cx, cy)))

    def test_bad_input(self):
        with self.assertRaises(ValueError):
            randPoint(0, (0, 0))
        with self.assertRaises(ValueError):
            randPoint(-0.5, (0, 0))


if __name__ == "__main__":
    unittest.main()
