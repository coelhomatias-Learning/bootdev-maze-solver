from window import Line, Point, Window


def main() -> None:
    win = Window(800, 600)

    p1, p2 = Point(200, 200), Point(600, 200)
    p3, p4 = Point(600, 400), Point(200, 400)
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p4)
    line4 = Line(p4, p1)

    win.draw_line(line1, "red")
    win.draw_line(line2, "red")
    win.draw_line(line3, "red")
    win.draw_line(line4, "red")

    win.wait_for_close()


if __name__ == "__main__":
    main()
