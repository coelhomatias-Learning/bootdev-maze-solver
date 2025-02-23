from tkinter import BOTH, Canvas, Tk


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, window: "Window", top_left: Point, bottom_right: Point) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._top_left = top_left
        self._top_right = Point(bottom_right.x, top_left.y)
        self._bottom_left = Point(top_left.x, bottom_right.y)
        self._bottom_right = bottom_right
        self._win = window
        self._fill_color = "black"

    def draw(self) -> None:
        if self.has_left_wall:
            self._win.draw_line(
                Line(self._bottom_left, self._top_left), self._fill_color
            )
        if self.has_top_wall:
            self._win.draw_line(Line(self._top_left, self._top_right), self._fill_color)
        if self.has_right_wall:
            self._win.draw_line(
                Line(self._top_right, self._bottom_right), self._fill_color
            )
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(self._bottom_right, self._bottom_left), self._fill_color
            )

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:
        center_self = Point(
            (self._top_left.x + self._bottom_right.x) // 2,
            (self._top_left.y + self._bottom_right.y) // 2,
        )
        center_to = Point(
            (to_cell._top_left.x + to_cell._bottom_right.x) // 2,
            (to_cell._top_left.y + to_cell._bottom_right.y) // 2,
        )
        color = "gray" if undo else "red"
        self._win.draw_line(Line(center_self, center_to), color)


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=width, height=height)
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

    def draw_cell(self, cell: Cell) -> None:
        cell.draw()

    def draw_cell_move(
        self, cell_from: Cell, cell_to: Cell, undo: bool = False
    ) -> None:
        cell_from.draw_move(cell_to, undo)
