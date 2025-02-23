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
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        self._cells: list[list[Cell]] = []
        self._create_and_draw_cells()

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

    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)
