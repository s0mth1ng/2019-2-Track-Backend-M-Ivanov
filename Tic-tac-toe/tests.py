import unittest
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_validator(self):
        self.assertEqual(self.g.make_move('1'), True)
        self.assertEqual(self.g.make_move('1'), False)
        self.assertEqual(self.g.make_move('-1'), False)
        self.assertEqual(self.g.make_move('02'), False)
        self.assertEqual(self.g.make_move('10'), False)
        self.assertEqual(self.g.make_move(''), False)
        self.assertEqual(self.g.make_move('asd'), False)
        self.assertEqual(self.g.make_move(' '), False)
        self.assertEqual(self.g.make_move('2'), True)

    def test_win_checker(self):
        self.g.board = list('XXXOO6789')
        self.assertEqual(self.g.check_win(), True)

        self.g.board = list('X2XOOOX89')
        self.assertEqual(self.g.check_win(), True)

        self.g.board = list('123456789')
        self.assertEqual(self.g.check_win(), False)

        self.g.board = list('XOXOXOOXO')
        self.assertEqual(self.g.check_win(), False)

        self.g.board = list('XOXOXOX89')
        self.assertEqual(self.g.check_win(), True)

        self.g.board = list('XO3XO6X89')
        self.assertEqual(self.g.check_win(), True)


if __name__ == '__main__':
    unittest.main()
