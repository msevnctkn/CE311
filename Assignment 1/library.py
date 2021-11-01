#
#   Purpose of this library is that help the drawings about Structural Drawings
#
#
#   Author: Muhammed SEVİNÇTEKİN
#
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as p
from sympy.solvers import solve
from sympy import Symbol


class Tool:
    def __init__(self):
        pass

    # Memory Allocation
    def __delete__(self, instance):
        # Free memory
        del instance

    def __str__(self):
        # TO DO
        # Call any iterable object.
        pass

    def roller_support(self, **kwargs):
        """
        :param
            x       -> x - location of roller support   (float)     ->  (mandatory)
            y       -> y - location of roller support   (float)     ->  (mandatory)
            r       ->  radius of roller support        (float)     ->  (mandatory)
            color   ->  color of roller support         (string)    ->  (optional)

        """
        if not "color" in kwargs:
            kwargs["color"] = "black"


        x = kwargs["x"]
        y = kwargs["y"]
        r = kwargs["r"]
        color = kwargs["color"]

        circle = plt.Circle((x, y), radius=r, fc=color, ec=color)
        plt.gca().add_patch(circle)


        """
        rl_x = [35, 10.75]
        rl_y = [70 - 2 * r, 10 - 2 * r]
        roller_line = plt.Line2D(rl_x, rl_y, color="black")
        ax.add_line(roller_line)
        """

    def pinned_support(self, **kwargs):

        """
        :param
            x       ->  x - location of upper point of triangle -> float    ->  (mandatory)
            y       ->  y - location of upper point of triangle -> float    ->  (mandatory)
            r       ->  radius                                  -> float    ->  (mandatory)
            color   ->  pinned support color                    -> string   ->  (optional)
        """

        if not "color" in kwargs:
            kwargs["color"] = "black"

        # triangle for pinned support
        points = np.array([[kwargs["x"], kwargs["y"]], [kwargs["x"] - 2 * kwargs["r"], kwargs["x"] - 2 * kwargs["r"]],
                           [kwargs["x"] + 2 * kwargs["r"], kwargs["x"] - 2 * kwargs["r"]]])
        polygon = p.Polygon(points, closed=True, color=kwargs["color"])
        plt.gca().add_patch(polygon)

    def simple_beam(self, **kwargs):
        """
        :param
            x1          ->      x1 - location of beam   ->  float   (mandatory)
            y1          ->      y1 - location of beam   ->  float   (mandatory)
            x2          ->      x2 - location of beam   ->  float   (mandatory)
            y2          ->      y2 - location of beam   ->  float   (mandatory)
            color       ->      color of beam           ->  string  (optional)
            linewidth   ->      line width of beam      ->  string  (optional)

        """

        if not "linewidth" in kwargs:
            kwargs["linewidth"] = 3

        if not "color" in kwargs:
            kwargs["color"] = "black"

        x = [kwargs["x1"], kwargs["x2"]]
        y = [kwargs["y1"], kwargs["y2"]]

        line = plt.Line2D(x, y, color=kwargs["color"], linewidth=kwargs["linewidth"])
        ax.add_line(line)

    def uniform_distributed_load(self, **kwargs):
        """
        :param
            x1      ->      x1 - left down position of D.L      ->  float   (mandatory)
            y1      ->      y1 - left down position of D.L      ->  float   (mandatory)
            x2      ->      x2 - right down position of D.L     ->  float   (mandatory)
            y2      ->      y2 - right down position of D.L     ->  float   (mandatory)
            text    ->      text                                ->  string  (optional)

        """

        height = 2
        self.simple_beam(x1=kwargs["x1"], y1=kwargs["y1"], x2=kwargs["x2"], y2=kwargs["y2"], color=kwargs["color"], linewidth=1)
        self.simple_beam(x1=kwargs["x1"], y1=kwargs["y1"] + height, x2=kwargs["x2"],
                         y2=kwargs["y2"] + height, color=kwargs["color"], linewidth=1)
        length = int(abs(kwargs["x1"] - kwargs["x2"]))

        for i in range(0, int(length+1), 2):
            plt.arrow(kwargs["x1"]+i, kwargs["y1"]+2, 0, -1, head_width=1, head_length=1, color=kwargs["color"])

        text = ""
        if not "text" in kwargs:
            kwargs["text"] = ""
        else:
            kwargs["text"] = text


    def triangular_distributed_load(self, **kwargs):
        height = 5
        width = 5

        self.simple_beam(x1=kwargs["x1"], y1=kwargs["y1"], x2=kwargs["x2"],
                         y2=kwargs["y2"], color=kwargs["color"], linewidth=1)

        self.simple_beam(x1=kwargs["x1"], y1=kwargs["y1"], x2=kwargs["x2"],
                         y2=kwargs["y2"] + height, color=kwargs["color"], linewidth=1)

        self.simple_beam(x1=kwargs["x2"], y1=kwargs["y2"]+height, x2=kwargs["x2"],
                         y2=kwargs["y2"], color=kwargs["color"], linewidth=1)

        length = int(abs(kwargs["x1"] - kwargs["x2"]))
        inc = -1

        for i in range(0, int(length + 1), 2):
            inc -= 1
            plt.arrow(kwargs["x1"] + i, kwargs["y2"] + 2, 0, inc, head_width=1,
                      head_length=1, color=kwargs["color"])

    def trapezoidal_distributed_load(self):
        # TO DO
        pass

    def single_load(self, *args, **kwargs):
        plt.arrow(x=kwargs["x"], y=kwargs["y"], dx=kwargs["dx"], dy=kwargs["dy"], color=kwargs["color"], head_width=1, head_length=1)



fig = plt.figure()
ax = fig.add_subplot()