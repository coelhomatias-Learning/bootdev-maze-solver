from tkinter import BOTH, Canvas, Tk

from graphics import Cell, Line


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(
            self.__root, width=width, height=height, background="white"
        )
        self.__canvas.pack(fill=BOTH, expand=1)
        self.is_running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self) -> None:
        self.is_running = False

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.__canvas, fill_color)

    def draw_lines(self, lines: list[Line], fill_color: str) -> None:
        for line in lines:
            self.draw_line(line, fill_color)

    def draw_cell(self, cell: Cell) -> None:
        cell.draw(self.__canvas)

    def draw_cells(self, cells: list[Cell]) -> None:
        for cell in cells:
            self.draw_cell(cell)

    def draw_cell_move(
        self, cell_from: Cell, cell_to: Cell, undo: bool = False
    ) -> None:
        color = "gray" if undo else "red"
        self.draw_line(Line(cell_from._center_point, cell_to._center_point), color)
