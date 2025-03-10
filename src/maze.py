import random
import time

from graphics import Cell, Point
from window import Window


class Maze:
    def __init__(
        self,
        x1: float,
        y1: float,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window | None = None,
        seed: int | None = None,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)

        self._cells: list[list[Cell]] = []
        self._create_and_draw_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _break_entrance_and_exit(self) -> None:
        if not self._cells:
            return
        first, last = self._cells[0][0], self._cells[-1][-1]
        first.has_top_wall = False
        last.has_bottom_wall = False
        self._animate()

    def _break_wall_between_cells(self, indx1: tuple[int, int], indx2) -> None:
        if not self._cells:
            return

        i1, j1 = indx1
        i2, j2 = indx2

        c1 = self._cells[i1][j1]
        c2 = self._cells[i2][j2]

        if i1 == i2 and j1 == j2:
            return
        elif j1 == j2:
            if i1 == (i2 - 1):
                c1.has_right_wall = False
                c2.has_left_wall = False
            elif i1 == (i2 + 1):
                c1.has_left_wall = False
                c2.has_right_wall = False
        elif i1 == i2:
            if j1 == (j2 - 1):
                c1.has_bottom_wall = False
                c2.has_top_wall = False
            elif j1 == (j2 + 1):
                c1.has_top_wall = False
                c2.has_bottom_wall = False
        else:
            return

        self._animate()

    def _break_walls_r(self, i: int, j: int) -> None:
        if not self._cells:
            return
        self._cells[i][j].visited = True

        while True:
            to_visit: list[tuple[int, int]] = []

            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if not to_visit:
                return
            choice = random.choice(to_visit)
            self._break_wall_between_cells((i, j), choice)
            self._break_walls_r(*choice)

    def _reset_cells_visited(self) -> None:
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _create_cells(self) -> None:
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                c1, c2 = (
                    Point(
                        self.x1 + i * self.cell_size_x, self.y1 + j * self.cell_size_y
                    ),
                    Point(
                        self.x1 + (i + 1) * self.cell_size_x,
                        self.y1 + (j + 1) * self.cell_size_y,
                    ),
                )
                cell = Cell(c1, c2)
                col.append(cell)
            self._cells.append(col)

    def _create_and_draw_cells(self) -> None:
        if self._win is None:
            return
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                c1, c2 = (
                    Point(
                        self.x1 + i * self.cell_size_x, self.y1 + j * self.cell_size_y
                    ),
                    Point(
                        self.x1 + (i + 1) * self.cell_size_x,
                        self.y1 + (j + 1) * self.cell_size_y,
                    ),
                )
                cell = Cell(c1, c2)
                col.append(cell)
                self._win.draw_cell(cell)
                self._animate()
            self._cells.append(col)

    def _draw_cell(self, cell: Cell):
        if self._win is None:
            return
        self._win.draw_cell(cell)
        self._animate()

    def _draw_cells(self):
        if self._win is None or not self._cells:
            return
        for col in self._cells:
            for cell in col:
                self._win.draw_cell(cell)
                self._animate()

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, i: int, j: int) -> bool:
        if not self._cells or not self._win:
            return False

        self._animate()

        current_cell = self._cells[i][j]
        current_cell.visited = True

        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True

        to_visit: list[tuple[int, int]] = []

        if (
            i > 0
            and not self._cells[i - 1][j].visited
            and not current_cell.has_left_wall
        ):
            to_visit.append((i - 1, j))
        if (
            i < self.num_cols - 1
            and not self._cells[i + 1][j].visited
            and not current_cell.has_right_wall
        ):
            to_visit.append((i + 1, j))
        if (
            j > 0
            and not self._cells[i][j - 1].visited
            and not current_cell.has_top_wall
        ):
            to_visit.append((i, j - 1))
        if (
            j < self.num_rows - 1
            and not self._cells[i][j + 1].visited
            and not current_cell.has_bottom_wall
        ):
            to_visit.append((i, j + 1))

        for to_idx in to_visit:
            to_cell = self._cells[to_idx[0]][to_idx[1]]
            self._win.draw_cell_move(current_cell, to_cell)
            if self._solve_r(*to_idx):
                return True
            self._win.draw_cell_move(current_cell, to_cell, True)

        return False

    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)
