import unittest
import Solution_3


class PartOneTest(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(Solution_3.part_one(memory="xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"), 161)
    

class PartTwoTest(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(Solution_3.part_two(memory="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"), 48)
        self.assertEqual(Solution_3.part_two(memory="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(43,395))"), 16993)
        
    def test_end_on_dont(self):
        self.assertEqual(Solution_3.part_two(memory="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(43,395))don't()mul(435,453)fsdendmul(56,77)"), 16993) # ends on don't
    
    def test_multiple_donts(self):
        self.assertEqual(Solution_3.part_two(memory="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64]don't()(mul(11,8)undo()?mul(43,395))don't()mul(435,453)fsdendmul(56,77)"), 16993) # multiple don'ts
    
    def test_multiple_dos(self):
        self.assertEqual(Solution_3.part_two(memory="xmul(2,4)&mul[3,7]!do()fsdmul(1,1)^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(43,395))don't()mul(435,453)fsdendmul(56,77)"), 16994) # multiple dos


if __name__ == '__main__':
    unittest.main()