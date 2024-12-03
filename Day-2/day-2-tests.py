import unittest
import Solution_2


class TestPartTwo(unittest.TestCase):
    def test_safe_report(self):
        self.assertEqual(Solution_2.part_two([[1, 3, 5, 6, 7]]), 1)
        self.assertEqual(Solution_2.part_two([[7, 6, 4, 2, 1]]), 1)
        self.assertEqual(Solution_2.part_two([[1, 2, 7, 8, 9]]), 0)
        self.assertEqual(Solution_2.part_two([[7, 6, 4, 1]]), 1)
    
    def test_bad_level_tolerance(self):
        self.assertEqual(Solution_2.part_two([[1, 3, 2, 4, 5]]), 1)
        self.assertEqual(Solution_2.part_two([[8, 6, 4, 4, 1]]), 1)
        self.assertEqual(Solution_2.part_two([[7, 7, 6, 4, 1]]), 1)
        self.assertEqual(Solution_2.part_two([[7, 6, 6, 4, 1]]), 1)
        self.assertEqual(Solution_2.part_two([[7, 6, 4, 4, 1]]), 1)
        self.assertEqual(Solution_2.part_two([[7, 6, 4, 1, 1]]), 1)

        self.assertEqual(Solution_2.part_two([[10, 8, 6, 4, 1]]), 1)
        self.assertEqual(Solution_2.part_two([[7, 14, 6, 4, 1]]), 1)
        self.assertEqual(Solution_2.part_two([[7, 6, 20, 4, 1]]), 1)
        self.assertEqual(Solution_2.part_two([[7, 6, 4, 44, 1]]), 1)
        self.assertEqual(Solution_2.part_two([[7, 6, 5, 4, 55]]), 1)


if __name__ == '__main__':
    unittest.main()
