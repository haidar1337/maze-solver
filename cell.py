from line import Line
from point import Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        center_x = (self._x1+self._x2)/2
        center_y = (self._y1+self._y2)/2
        other_center_x = (to_cell._x2+to_cell._x1)/2
        other_center_y = (to_cell._y2+to_cell._y1)/2

        center = Point(center_x, center_y)
        other_center = Point(other_center_x, other_center_y)

        line = Line(center, other_center)
        fill_color = "red"
        if undo == True:
            fill_color = "gray"
        self._win.draw_line(line, fill_color)
