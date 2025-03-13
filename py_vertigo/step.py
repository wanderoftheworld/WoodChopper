import unittest

def getStepCount(input: str) -> int:
    num = int(input, 2)
    if num <= 0:
        raise ValueError("Require a positive integer as input")
    steps = 0
    while num > 1:
        if num % 2 == 0:
            num = num >> 1
        else:
            num += 1
        steps += 1
    return steps

class TestGetStepCount(unittest.TestCase):
    def test_good_input(self):
        self.assertEqual(1, getStepCount('10'))
        self.assertEqual(1, getStepCount('0b10'))
        self.assertEqual(3, getStepCount('11'))
        self.assertEqual(3, getStepCount('0b11'))

    def test_bad_string(self):
        with self.assertRaises(ValueError):
            getStepCount('3')

    def test_bad_input_type(self):
        with self.assertRaises(TypeError):
            getStepCount(3)

    def test_negative_or_zero(self):
        with self.assertRaises(ValueError):
            getStepCount('-0b1')
        with self.assertRaises(ValueError):
            getStepCount('0')

    def test_big_int(self):
        self.assertEqual(33, getStepCount('0b11111111111111111111111111111111'))

if __name__ == "__main__":
    unittest.main()
