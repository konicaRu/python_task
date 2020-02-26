import unittest
import MergeSort


class MyTestCase(unittest.TestCase):
    def test_one(self):
        a = [2]
        self.assertEqual(MergeSort.MergeSort(a) == sorted(a), True)

    def test_two(self):
        a = [2, 1]
        self.assertEqual(MergeSort.MergeSort(a) == sorted(a), True)

    def test_tree(self):
        a = [2, 1, 10]
        self.assertEqual(MergeSort.MergeSort(a) == sorted(a), True)

    def test_four(self):
        a = [2, 1, 10, 11]
        self.assertEqual(MergeSort.MergeSort(a) == sorted(a), True)

    def test_seven(self):
        a = [2, 1, 3, 4, 8, 5, 6]
        self.assertEqual(MergeSort.MergeSort(a) == sorted(a), True)

    def test_seven2(self):
        a = [6, 5, 8, 4, 2, 1, 3]
        self.assertEqual(MergeSort.MergeSort(a) == sorted(a), True)

    def test_eith(self):
        a = [5, 1, 7, 4, 6, 8, 11, 10]
        self.assertEqual(MergeSort.MergeSort(a) == sorted(a), True)

    def test_fourteen(self):
        a = [12, 11, 15, 7, 5, 6, 4, 3, 1, 2, 87, 98, 70, 23]
        self.assertEqual(MergeSort.MergeSort(a) == sorted(a), True)


if __name__ == '__main__':
    unittest.main()
