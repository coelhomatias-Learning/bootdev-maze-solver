from tkinter import Canvas


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2
        self._id: int | None = None
        self._canvas: Canvas | None = None

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        self._canvas = canvas
        self._id = self._canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )

    def delete(self) -> None:
        if not self._id or not self._canvas:
            return
        self._canvas.delete(self._id)
        self._id = None
        self._canvas = None


class Cell:
    def __init__(self, top_left: Point, bottom_right: Point) -> None:
        self._top_left = top_left
        self._top_right = Point(bottom_right.x, top_left.y)
        self._bottom_left = Point(top_left.x, bottom_right.y)
        self._bottom_right = bottom_right
        self._walls: list[Line | None] = [
            Line(self._bottom_left, self._top_left),
            Line(self._top_left, self._top_right),
            Line(self._top_right, self._bottom_right),
            Line(self._bottom_right, self._bottom_left),
        ]
        self._center_point = Point(
            (self._top_left.x + self._bottom_right.x) // 2,
            (self._top_left.y + self._bottom_right.y) // 2,
        )
        self._fill_color = "black"
        self.visited = False

    @property
    def has_left_wall(self):
        return self._walls[0] is not None

    @has_left_wall.setter
    def has_left_wall(self, val: bool):
        if val:
            if self._walls[0] is not None:
                return
            self._walls[0] = Line(self._bottom_left, self._top_left)
        else:
            if not self._walls[0]:
                return
            self._walls[0].delete()
            self._walls[0] = None

    @property
    def has_top_wall(self):
        return self._walls[1] is not None

    @has_top_wall.setter
    def has_top_wall(self, val: bool):
        if val:
            if self._walls[1] is not None:
                return
            self._walls[1] = Line(self._top_left, self._top_right)
        else:
            if not self._walls[1]:
                return
            self._walls[1].delete()
            self._walls[1] = None

    @property
    def has_right_wall(self):
        return self._walls[2] is not None

    @has_right_wall.setter
    def has_right_wall(self, val: bool):
        if val:
            if self._walls[2] is not None:
                return
            self._walls[2] = Line(self._top_right, self._bottom_right)
        else:
            if not self._walls[2]:
                return
            self._walls[2].delete()
            self._walls[2] = None

    @property
    def has_bottom_wall(self):
        return self._walls[3] is not None

    @has_bottom_wall.setter
    def has_bottom_wall(self, val: bool):
        if val:
            if self._walls[3] is not None:
                return
            self._walls[3] = Line(self._bottom_right, self._bottom_left)
        else:
            if not self._walls[3]:
                return
            self._walls[3].delete()
            self._walls[3] = None

    def draw(self, canvas: Canvas) -> None:
        for wall in self._walls:
            if wall is not None:
                wall.draw(canvas, self._fill_color)
