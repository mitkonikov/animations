from manim import *

class GraphFunc(Scene):
    def construct(self):
        # Set constants
        N = 16
        x_min, x_max, x_step = 0.1, 20, 1
        y_min, y_max, y_step = 0.1, 20, 1

        # Create axes
        axes = Axes(
            x_range=[x_min, x_max, x_step],
            y_range=[y_min, y_max, y_step],
            x_length=7,
            y_length=5,
            axis_config={"include_tip": True},
            # x_axis_label="$B$",
            # y_axis_label="$f(B)$"
        )

        # Define function
        def func(t):
            x = t
            y = N / x + x
            return axes.c2p(x, y)

        # Create graph
        graph = ParametricFunction(func, t_range=[x_min, x_max], color=BLUE)

        # Add labels to graph
        graph_label = axes.get_graph_label(graph, "f(B) = \\frac{N}{B} + B", x_val=3, direction=UP * 5 + RIGHT, buff=0.3)

        # Add points to graph
        points = VGroup()
        for i in range(1, int((x_max - x_min) / x_step) + 1):
            x = x_min + i * x_step
            y = N / x + x
            point = Dot(axes.c2p(x, y), color=RED)
            points.add(point)

        # Create animations
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.play(Create(points))

        # Animate function
        anims = []
        for i in range(1, len(points)):
            line = Line(points[i-1].get_center(), points[i].get_center(), color=YELLOW)
            anims.append(Create(line))
        self.play(*anims, run_time=0.5)

        self.wait()

        T = 1
        W = 1
        self.wait(W)
        t = MathTex("f(B) = \\frac{N + B^2}{B}").shift(DOWN + RIGHT)
        self.play(Write(t), run_time=T)
        self.wait(W)
        td = MathTex("f'(B) = 1 - \\frac{N}{B^2}").shift(DOWN + RIGHT)
        self.play(Transform(t, td), run_time=T)
        self.wait(W)
        td2 = MathTex("0 = 1 - \\frac{N}{B^2}").shift(DOWN + RIGHT)
        self.play(Transform(t, td2), run_time=T)
        self.wait(W)
        td3 = MathTex("1 = \\frac{N}{B^2}").shift(DOWN + RIGHT)
        self.play(Transform(t, td3), run_time=T)
        self.wait(W)
        td4 = MathTex("N = B^2").shift(DOWN + RIGHT)
        self.play(Transform(t, td4), run_time=T)
        self.wait(W)
        td5 = MathTex("B = \\sqrt{N}").shift(DOWN + RIGHT)
        self.play(Transform(t, td5), run_time=T)
        self.wait(W)
        
        self.wait(3)