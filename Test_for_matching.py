import unittest
from memory_game import create_board, check_match, mark_matched


class TestMemoryGame(unittest.TestCase):

    def test_create_board_size(self):
        board = create_board()
        self.assertEqual(len(board), 4)
        for row in board:
            self.assertEqual(len(row), 4)

    def test_board_has_pairs(self):
        board = create_board()
        values = []
        for row in board:
            for value, status in row:
                values.append(value)

        self.assertEqual(len(values), 16)

        for number in set(values):
            self.assertEqual(values.count(number), 2)

    def test_check_match_true(self):
        board = [
            [(1, "hidden"), (2, "hidden")],
            [(1, "hidden"), (3, "hidden")]
        ]
        self.assertTrue(check_match(board, (0, 0), (1, 0)))

    def test_check_match_false(self):
        board = [
            [(1, "hidden"), (2, "hidden")],
            [(3, "hidden"), (4, "hidden")]
        ]
        self.assertFalse(check_match(board, (0, 0), (0, 1)))

    def test_mark_matched(self):
        board = [
            [(1, "hidden"), (1, "hidden")]
        ]
        mark_matched(board, (0, 0), (0, 1))
        self.assertEqual(board[0][0][1], "matched")
        self.assertEqual(board[0][1][1], "matched")


if __name__ == "__main__":
    unittest.main()