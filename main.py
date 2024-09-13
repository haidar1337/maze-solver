from line import Line
from point import Point
from window import Window


def main():
    win = Window(800, 600)
    line = Line(Point(4, 6), Point(6, 6))
    line2 = Line(Point(20, 500), Point(2, 5))
    win.draw_line(line, "red")
    win.draw_line(line2, "black")
    win.wait_for_close()

main()