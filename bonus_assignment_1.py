#
#   GEBZE TECHNICAL UNIVERSITY - THEORY OF STRUCTURE 1 CE311 - BONUS ASSIGNMENT 1
#   Date    : 10.10.2021 - 16.10
#   Author  : Muhammed
#
#

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as p
from sympy.solvers import solve
from sympy import Symbol


class Simple_Beam:
    def __init__(self):

        #Variable
        self.p_load = 20  # kN
        self.length_of_beam = 10  # kN

    def plot_simple_beam(self):
        fig = plt.figure()
        ax = fig.add_subplot()
        plt.axis('equal')


        # arrow for single load
        plt.arrow(20, 13, 0, -2, head_width=1, head_length=0.75)
        plt.text(18.5, 13, "20 kN", size=15)


        # line for simple beam
        x = [10, 30]
        y = [10, 10]
        line = plt.Line2D(x, y, color="black", linewidth=4)
        ax.add_line(line)
        plt.text(9, 10.5, "A", size=16)
        plt.text(30, 10.5, "B", size=16)
        plt.text(19, 8, "10m", size=10)


        # circle for roller support
        r = .3
        circle = plt.Circle((30, 10 - r), radius=r, fc="black", ec="black")
        plt.gca().add_patch(circle)
        rl_x = [9.25, 10.75]
        rl_y = [10 - 2 * r, 10 - 2 * r]
        roller_line = plt.Line2D(rl_x, rl_y, color="black")
        ax.add_line(roller_line)


        # triangle for pinned support
        points = np.array([[10, 10], [10 - 2 * r, 10 - 2 * r], [10 + 2 * r, 10 - 2 * r]])
        polygon = p.Polygon(points, closed=True, color="black")
        plt.gca().add_patch(polygon)

        plt.show()

    def calculations(self):

        # taking Moment at point A for By
        By = Symbol("By")
        Eq = self.p_load * self.length_of_beam/2 - By * self.length_of_beam
        By = solve(Eq)[0]
        print("By: ", str(By) + " kN (upward)")

        # taking Moment at point B for Ay
        Ay = Symbol("Ay")
        Eq2 = Ay * self.length_of_beam - self.p_load * self.length_of_beam / 2
        Ay = solve(Eq2)[0]
        print("Ay: ", str(Ay) + " kN (upward)")

        # for Ax
        Ax = Symbol("Ax")
        Eq3 = Ax
        Ax = solve(Eq3)[0]
        print("Ax: ", Ax)

        # control condition, Total Fy = 0;
        Fy = Symbol("Fy")
        Eq4 = Ay + By - self.p_load + Fy
        Fy = solve(Eq4)[0]
        print("Total Force on y-axis: ", Fy)



sb = Simple_Beam()
while True:
    option = (input("\n\n\nEnter your selection:\n"
                       "1 - Show the Simple Supported Beam Set-up\n"
                       "2 - Show the result of support reactions\n"
                       "q - Quit\n\n\n"))
    if option == "1":
        sb.plot_simple_beam()
    elif option == "2":
        sb.calculations()
    elif option == "q":
        break
    else:
        print("Incorrect input")

