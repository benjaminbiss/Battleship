from typing import Union
import unittest
from unittest.main import main
import gameboard

class TestGameboard(unittest.TestCase):

    def setUp():
        pass

    def test_gameboard(self):
        board = gameboard.Gameboard()
        board.create_board()

if __name__ == '__main__':
    unittest.main()