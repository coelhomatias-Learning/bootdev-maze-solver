from maze import Maze
from window import Window


def main() -> None:
    win = Window(800, 600)

    maze = Maze(100, 100, 8, 12, 50, 50, win)
    maze._break_walls_r(0, 0)

    win.wait_for_close()


if __name__ == "__main__":
    main()
