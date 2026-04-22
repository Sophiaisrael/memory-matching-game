import unittest
from memory_game import create_board, all_matched


class TestMemoryGame(unittest.TestCase):

    def test_create_board_size(self):
        board = create_board(2)
        self.assertEqual(len(board), 4)
        for row in board:
            self.assertEqual(len(row), 4)

    def test_values_match_size_2(self):
        board = create_board(2)
        values = [v for row in board for v, _ in row]

        self.assertEqual(len(values), 16)

        for val in set(values):
            self.assertEqual(values.count(val), 2)

    def test_values_match_size_4(self):
        board = create_board(4)
        values = [v for row in board for v, _ in row]

        self.assertEqual(len(values), 16)

        for val in set(values):
            self.assertEqual(values.count(val), 4)

    def test_all_matched_false(self):
        board = create_board(2)
        self.assertFalse(all_matched(board))

    def test_all_matched_true(self):
        board = [[(1, "matched") for _ in range(4)] for _ in range(4)]
        self.assertTrue(all_matched(board))


if __name__ == "__main__":
    unittest.main()
