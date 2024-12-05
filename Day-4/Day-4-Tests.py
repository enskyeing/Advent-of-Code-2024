import unittest
import Solution_4

WORD_SEARCH_TEXT = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
"""

WORD_SEARCH = [row.strip() for row in WORD_SEARCH_TEXT.splitlines()]

# class PartOneTests(unittest.TestCase):
#     def test_answer(self):
#         self.assertEqual(Solution_4.part_one(word_search=WORD_SEARCH, word="XMAS"), 18)

class PartTwoTests(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(Solution_4.part_two(board=WORD_SEARCH, word="MAS"), 5)


if __name__ == "__main__":
    unittest.main()