from typing import List
from manim import *
from colors import CYAN

class AbsPlots(Scene):
    def f(self, x, points):
        return sum(abs(point - x) for point in points)

    def construct(self):
        axes = Axes(
            x_range=[-2, 15, 1],
            y_range=[-2, 30, 5],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-2, 15.1, 1),
                "numbers_with_elongated_ticks": np.arange(-2, 15.1, 1),
            },
            tips=False,
        )

        x_axis_label = Tex("$x$").move_to(axes.get_x_axis()).shift(RIGHT * 5.5 + UP * 0.5)
        y_axis_label = Tex("cost").move_to(axes.get_y_axis()).shift(UP * 2.5 + RIGHT * 0.8)

        points = [2, 5, 12]

        abs_graph = axes.plot(lambda x: self.f(x, points), color=BLUE)
        abs_label = axes.get_graph_label(abs_graph, "f(x)", x_val=2, direction=UP * 3)
        
        lines = []
        for i in range(len(points)):
            lines.append(axes.get_vertical_line(
                axes.i2gp(points[i], abs_graph), color=YELLOW, line_func=Line
            ).set_z_index(-1000))

        plot = VGroup(abs_graph, abs_label, x_axis_label, y_axis_label)
        self.play(FadeIn(axes))
        self.wait(2)
        
        dots = []
        for i in range(len(points)):
            location = axes.coords_to_point(points[i], 0)
            dots.append(Dot(location))
            dots.append(ImageMobject("./people/" + str(i + 1) + ".png").scale(0.15).move_to(location).shift(UP * 0.4))

        self.play(*list(map(FadeIn, dots)))
        self.wait(5)
        self.play(DrawBorderThenFill(plot), *list(map(FadeIn, lines)))
        self.wait(10)

        ### =======================================
        ###     DECREASING
        ### =======================================
        t = ValueTracker(-1)

        initial_point = [axes.coords_to_point(t.get_value(), self.f(t.get_value(), points))]
        dot = Dot(point=initial_point)

        dot.add_updater(lambda x: x.move_to(axes.c2p(t.get_value(), self.f(t.get_value(), points))))
        x_space = np.linspace(-1, 5)
        minimum_index = self.f(x_space, points).argmin()

        # dec = MathTex('n - 2k \geq 0').shift(2 * UP)
        # dec2 = MathTex(r'k \leq \frac{n}{2}').shift(2 * UP)

        self.play(DrawBorderThenFill(dot))
        # self.play(DrawBorderThenFill(dot), Write(dec))
        # self.play(Transform(dec, dec2))
        self.play(t.animate.set_value(x_space[minimum_index]), run_time = 4)
        # self.wait(3)
        # self.play(FadeOut(dec))
        self.wait(2)

        ### =======================================
        ###     INCREASING
        ### =======================================
        # inc = MathTex('n - 2k \leq 0').shift(2 * UP)
        # inc2 = MathTex(r'k \geq \frac{n}{2}').shift(2 * UP)

        # self.play(DrawBorderThenFill(dot), Write(inc))
        # self.play(Transform(inc, inc2))
        self.play(t.animate.set_value(15), FadeOut(dot), run_time = 4)
        # self.wait(3)
        # self.play(FadeOut(inc))
        self.wait(10)

        initial_point = [axes.coords_to_point(5, self.f(5, points))]
        dot = Dot(point=initial_point, fill_color = RED)
        self.play(DrawBorderThenFill(dot))
        self.play(dots[3].animate.scale(1.8).shift(UP * 0.2))
        self.wait(10)

        # self.play(FadeOut(dot))
        # t.set_value(-1)
        # self.play(FadeIn(dot))
        # self.play(t.animate.set_value(6), run_time = 4)
        # self.wait(1)
        # self.play(t.animate.set_value(18), run_time = 4)
        # self.wait(2)

        # stationary = MathTex('n - 2k = 0').shift(2 * UP)
        # stationary2 = MathTex(r'k = \frac{n}{2}').shift(2 * UP)

        # self.play(Write(stationary))
        # self.wait(2)
        # self.play(Transform(stationary, stationary2))
        
        # self.wait(2)