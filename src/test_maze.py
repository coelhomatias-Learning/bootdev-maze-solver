import unittest

from maze import Maze


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._create_cells()
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        m1._create_cells()
        m1._break_entrance_and_exit()

        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall)

    def test_break_between_walls_vertical(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        m1._create_cells()
        m1._break_entrance_and_exit()
        m1._break_wall_between_cells((0, 1), (0, 0))

        self.assertFalse(m1._cells[0][1].has_top_wall)
        self.assertFalse(m1._cells[0][0].has_bottom_wall)

    def test_break_between_walls_horizontal(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        m1._create_cells()
        m1._break_entrance_and_exit()
        m1._break_wall_between_cells((0, 0), (1, 0))

        self.assertFalse(m1._cells[1][0].has_left_wall)
        self.assertFalse(m1._cells[0][0].has_right_wall)

    def test_break_between_walls_diagonal(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        m1._create_cells()
        m1._break_entrance_and_exit()
        result = m1._break_wall_between_cells((2, 2), (1, 1))

        self.assertIsNone(result)
        self.assertTrue(m1._cells[2][2].has_left_wall)
        self.assertTrue(m1._cells[2][2].has_top_wall)
        self.assertTrue(m1._cells[2][2].has_right_wall)
        self.assertTrue(m1._cells[2][2].has_bottom_wall)
        self.assertTrue(m1._cells[1][1].has_left_wall)
        self.assertTrue(m1._cells[1][1].has_top_wall)
        self.assertTrue(m1._cells[1][1].has_right_wall)
        self.assertTrue(m1._cells[1][1].has_bottom_wall)

    # TODO: Write tests for maze._adjacent_cells


if __name__ == "__main__":
    unittest.main()
