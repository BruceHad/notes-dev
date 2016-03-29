import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_1(self):
        """Test for an empty list"""
        list1 = []
        list1_expected = []
        a1.swap_k(list1, 0)
        self.assertEqual(list1, list1_expected)

    def test_swap_k_2(self):
        """Test for a one-element list"""
        list1 = [1]
        list1_expected = [1]
        a1.swap_k(list1, 0)
        self.assertEqual(list1, list1_expected)

    def test_swap_k_3(self):
        """Test for a two-element list"""
        list1 = [1, 2]
        list1_expected = [2, 1]
        a1.swap_k(list1, 1)
        self.assertEqual(list1, list1_expected)


    def test_swap_k_4(self):
        """Test for a three element list"""
        list1 = [1, 2, 3]
        list1_expected = [3, 2, 1]
        a1.swap_k(list1, 1)
        self.assertEqual(list1, list1_expected)

    def test_swap_k_5(self):
        """Test for a longer list with even number of elements"""
        list1 = [1, 2, 3, 4, 5, 6, 7, 8]
        list1_expected = [5, 6,7 , 8, 1, 2, 3, 4]
        a1.swap_k(list1, 4)
        self.assertEqual(list1, list1_expected)

    def test_swap_k_6(self):
        """Test for a longer list with uneven number of elements"""
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        list1_expected = [8, 9, 10, 11, 5, 6, 7, 1, 2, 3, 4]
        a1.swap_k(list1, 4)
        self.assertEqual(list1, list1_expected)

    def test_swap_k_7(self):
        """Test for a longer list with k = 0"""
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        list1_expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        a1.swap_k(list1, 0)
        self.assertEqual(list1, list1_expected)

        
       

if __name__ == '__main__':
    unittest.main(exit=False)