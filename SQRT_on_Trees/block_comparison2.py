from manim import *
from random import randint

class BlockComparison2(Scene):
    def construct(self):
        def rf(x):
            if x < 0.5:
                return 16 * x * x * x * x * x
            return 1 - pow(-2 * x + 2, 5) / 2
        
        N = 40
        start = LEFT * 6
        circles = []
        ratio = 0.3
        def get_center(i):
            return start + RIGHT * i * ratio

        for i in range(N):
            c = Circle(0.05, color = BLUE, fill_color=BLUE, fill_opacity = 1)
            c.shift(get_center(i))
            circles.append(c)
            self.play(DrawBorderThenFill(c), run_time=0.05)

        tN = MathTex(f"N = {N}").shift(UP * 2 + LEFT * 2.5)
        self.play(Write(tN))
        
        B = 2
        tB = MathTex(f"B = {B}").shift(UP * 1.4 + LEFT * 2.5)
        self.play(Write(tB))

        dividers = []
        for i in range(B - 1):
            c1 = get_center((i + 1) * (N // B) - 1)
            c2 = get_center((i + 1) * (N // B))
            c = (c1 + c2) / 2
            l = Line(c + DOWN * 0.5, c + UP * 0.5)
            self.play(Create(l), run_time=0.1)
            dividers.append(l)

        self.wait(4)

        def indicate(r):
            c1 = get_center(r[0]) + DOWN * 0.3
            c2 = get_center(r[1] + 1) + DOWN * 0.3
            l = Line(c1, c2, stroke_width = 2)
            animations = [Create(l)]
            for i in range(r[0], r[1] + 2):
                animations.append(circles[i].animate.set_fill(RED))
                animations.append(circles[i].animate.set_color(RED))
            self.play(AnimationGroup(*animations))
            self.wait(4)

        indicate([8, 26])
        self.wait(5)

        self.play(FadeOut(tN), FadeOut(tB))
        return