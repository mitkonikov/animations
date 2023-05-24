from manim import *
from random import randint
from Utils.colors import SAT_GREEN

class Theorem(Scene):
    def construct(self):
        def rf(x):
            if x < 0.5:
                return 16 * x ** 5
            return 1 - pow(-2 * x + 2, 5) / 2
        
        g_def = MathTex("2 \\cdot \\log_2(8 \\cdot 10^9) \\approx 65").scale(1.2)
        acc = Text("* to be more accurate").scale(0.3).shift(DOWN * 0.6 + RIGHT * 1.3)
        self.play(FadeIn(g_def, shift=UP/2), FadeIn(acc, shift=UP/2), rate_func=rf)

        self.wait(2)
        return