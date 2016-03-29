import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_NumBuses1(self):
        """Test for n smaller than 50"""
        actual = a1.num_buses(49)
        expected = 1
        self.assertEqual(actual, expected)

    def test_NumBuses2(self):
        """Test for n equal 50"""
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)

    def test_NumBuses3(self):
        """Test for n higher than 50"""
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(actual, expected)

    def test_NumBuses2(self):
        """Test for n equal multiple of 50"""
        actual = a1.num_buses(500)
        expected = 10
        self.assertEqual(actual, expected)

    def test_NumBuses2(self):
        """Test for big n non divisible by 50"""
        actual = a1.num_buses(555)
        expected = 12
        self.assertEqual(actual, expected)
       

if __name__ == '__main__':
    unittest.main(exit=False)