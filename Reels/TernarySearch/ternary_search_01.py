from typing import List
from manim import *
from colors import CYAN

class AbsPlots(Scene):
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

        f = lambda x : pow(x-7, 2) / 3

        q_cont = axes.plot(f, color=RED, x_range=[3, 11, 0.01])
        q_cont_label = axes.get_graph_label(q_cont, "f(x)", x_val=2, direction=DOWN * 3 + RIGHT * 4)
        
        self.play(DrawBorderThenFill(axes))
        self.play(DrawBorderThenFill(q_cont))
        self.play(Write(q_cont_label))
        self.wait(5)

        save_disc = None

        sx = 1.5
        for rep in range(2):
            for i in range(5):
                off = rep * 5 * sx
                q_disc = axes.plot(lambda x: i if rep == 0 else 5-i, color=BLUE, x_range=[off + i * sx, off + (i + 1) * sx, 1])
                self.play(DrawBorderThenFill(q_disc), run_time = 0.2)
                
                if rep == 0 and i == 2:
                    save_disc = q_disc
        
        q_disc_label = axes.get_graph_label(save_disc, "g(x)", x_val=4, direction=UP*1.5)
        self.play(Write(q_disc_label), run_time = 0.5)
        self.wait(5)

        mn_point = [axes.coords_to_point(7, f(7))]
        dot = Dot(point=mn_point, radius=0.12)
        self.play(DrawBorderThenFill(dot))
        mn_text = Tex("minimum").move_to(mn_point, DOWN).shift(UP * 0.4 + RIGHT * 0.8)
        self.play(Write(mn_text))
        self.wait(5)

        mx_point = [axes.coords_to_point(8, 5)]
        dot2 = Dot(point=mx_point, radius=0.12)
        self.play(DrawBorderThenFill(dot2))
        mx_text = Tex("maximum").move_to(mx_point, DOWN).shift(UP * 0.4 + RIGHT * 0.8)
        self.play(Write(mx_text))
        self.wait(5)