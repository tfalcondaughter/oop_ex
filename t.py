import unittest

import f


class TestF(unittest.TestCase):
    def setUp(self):
        self.res = f.find_b('abbbbabbab')

    def test_word_abbbbabbab(self):
        self.assertEqual(self.res, (7, 4))


if __name__ == "__main__":
    unittest.main()
