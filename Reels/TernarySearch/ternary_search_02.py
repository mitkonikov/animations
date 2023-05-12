from typing import List
from manim import *
from Utils.colors import CYAN

class AbsPlots(Scene):
    def redraw_line(self, pos, axes: Axes, graph, text):
        line = axes.get_vertical_line(
            axes.i2gp(pos, graph), color=YELLOW, line_func=Line, stroke_width = 3
        ).set_z_index(-1000)

        text = Tex(text).move_to(line, DOWN).shift(DOWN * 0.7)
        self.play(DrawBorderThenFill(line), Write(text), run_time = 0.15)
        return [line, text]

    def draw_area(self, axes: Axes, graph, l, r):
        area = axes.get_area(graph, [l, r])
        self.add(area)
        return area

    def remove_lines(self, lines):
        self.play(*list(map(FadeOut, lines)))

    def construct(self):
        axes = Axes(
            x_range=[-2, 15, 1],
            y_range=[-2, 5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(0.0001, 15.1, 5),
                "numbers_with_elongated_ticks": np.arange(-2, 15.1, 1),
            },
            tips=False,
        )

        f = lambda x : pow(x-7, 2) / 5 * ((x + 5) * 0.05) + 1.4

        q_cont = axes.plot(f, color=RED, x_range=[1, 12, 0.01], stroke_width = 4)
        q_cont_label = axes.get_graph_label(q_cont, "f(x)", x_val=3, direction=UP * 3)
        
        self.play(DrawBorderThenFill(axes))
        self.play(DrawBorderThenFill(q_cont))
        self.play(Write(q_cont_label))
        self.wait(5)

        lines = []
        
        l = 1
        r = 12

        area = self.draw_area(axes, q_cont, l, r)

        while (r - l > 0.4):
            tmp = []
            if len(lines) >= 4:
                tmp = lines[:4]
                for i in range(4):
                    lines.pop(0)
                self.remove_lines([tmp[1], tmp[3]])
            
            lines.extend(self.redraw_line(l, axes, q_cont, "L"))
            lines.extend(self.redraw_line(r, axes, q_cont, "R"))

            if len(tmp) != 0:
                self.remove_lines([tmp[0], tmp[2]])

            self.play(FadeOut(area), run_time=0.2)
            area = self.draw_area(axes, q_cont, l, r)
            self.play(FadeIn(area), run_time=0.2)

            self.remove_lines(lines[:4])
            for i in range(4):
                lines.pop(0)

            mid1 = l + (r - l) / 3
            mid2 = l + (r - l) / 3 * 2

            lines.extend(self.redraw_line(mid1, axes, q_cont, "M1"))
            lines.extend(self.redraw_line(mid2, axes, q_cont, "M2"))
            
            if f(mid1) > f(mid2):
                l = mid1
            else:
                r = mid2

        self.remove_lines(lines)
        lines = []
        lines.extend(self.redraw_line((l + r) / 2, axes, q_cont, "M"))
        self.wait(4)