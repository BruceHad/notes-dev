import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_1(self):
        """ Test swap_k against empty set """
        nums = []
        a1.swap_k(nums, 0)
        actual = nums
        expected = []

    def test_swap_k_2(self):
        """ Test swap_k against two values """
        nums = [1,2]
        a1.swap_k(nums, 1)
        actual = nums
        expected = [2,1]
        
    def test_swap_k_3(self):
        """ Test swap_k against 5 number set """
        nums = [1, 2, 3, 4, 5]
        a1.swap_k(nums, 2)
        actual = nums
        expected = [4, 5, 3, 1, 2]

    def test_swap_k_4(self):
        """ Test swap_k against 6 number set """
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 3)
        actual = nums
        expected = [4, 5, 6, 1, 2, 3]

    def test_swap_k_5(self):
        """ Test swap_k with zero swaps """
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 0)
        actual = nums
        expected = [1, 2, 3, 4, 5, 6]

if __name__ == '__main__':
    unittest.main(exit=False)
