from graphics import Cell, Line, Point
from window import Window


def main() -> None:
    win = Window(800, 600)

    p1, p2 = Point(200, 200), Point(600, 200)
    p3, p4 = Point(600, 400), Point(200, 400)
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p4)
    line4 = Line(p4, p1)

    cp1, cp2 = Point(250, 250), Point(300, 300)
    cp3, cp4 = Point(300, 250), Point(350, 300)
    cell1 = Cell(cp1, cp2)
    cell2 = Cell(cp3, cp4)
    cell1.has_right_wall = False
    cell2.has_left_wall = False

    win.draw_line(line1, "red")
    win.draw_line(line2, "red")
    win.draw_line(line3, "red")
    win.draw_line(line4, "red")
    win.draw_cell(cell1)
    win.draw_cell(cell2)
    win.draw_cell_move(cell1, cell2)

    win.wait_for_close()


if __name__ == "__main__":
    main()
