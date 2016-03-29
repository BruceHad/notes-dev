import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary1(self):
        """Test for empty list"""
        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary2(self):
        """Test for handling zeros"""
        actual = a1.stock_price_summary([0, 0, 0])
        expected = (0,0)
        self.assertAlmostEqual(expected[0], actual[0])
        self.assertAlmostEqual(expected[1], actual[1]) 

    def test_stock_price_summary3(self):
        """Test for one gain"""
        actual = a1.stock_price_summary([1])
        expected = (1, 0)
        self.assertAlmostEqual(expected[0], actual[0])
        self.assertAlmostEqual(expected[1], actual[1])

    def test_stock_price_summary4(self):
        """Test for one loss"""
        actual = a1.stock_price_summary([-1])
        expected = (0, -1)
        self.assertAlmostEqual(expected[0], actual[0])
        self.assertAlmostEqual(expected[1], actual[1])

    def test_stock_price_summary5(self):
        """Test for handling floats"""
        actual = a1.stock_price_summary([0.01, -0.02])
        expected = (0.01, -0.02)
        self.assertAlmostEqual(expected[0], actual[0])
        self.assertAlmostEqual(expected[1], actual[1])

    def test_stock_price_summary6(self):
        """Test for a combination of many gains and loses in different formats"""
        actual = a1.stock_price_summary([0.1, -0.1, 0.01, 1, 0.5, 10, -10, - 1, - 0.01, -0.5])
        expected = (11.61, -11.61)
        self.assertAlmostEqual(expected[0], actual[0])
        self.assertAlmostEqual(expected[1], actual[1])

if __name__ == '__main__':
    unittest.main(exit=False)