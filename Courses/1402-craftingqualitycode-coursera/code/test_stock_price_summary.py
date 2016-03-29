import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_1(self):
        """ Test stock_price_summary against an empty set """
        actual = stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_2(self):
        """ Test stock_price_summary against two positive entries """
        actual = stock_price_summary([0.5, 0.7])
        expected = (1.2, 0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_3(self):
        """ Test stock_price_summary against two negative entries """
        actual = stock_price_summary([-0.5, -0.7])
        expected = (0, -1.2)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_4(self):
        """ Test stock_price_summary against two mixed entries """
        actual = stock_price_summary([-0.5, 0.7])
        expected = (0.7, -0.5)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_5(self):
        """ Test stock_price_summary against numerous entries """
        actual = stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main(exit=False)
