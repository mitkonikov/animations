from typing import List
from manim import *
from colors import CYAN

class AddSum(Scene):
    def construct(self):
        big_sum = MathTex(r'\displaystyle \sum_{i=1}^{n} \; \lvert x_{i} - x \rvert').scale(1.5)
        self.play(DrawBorderThenFill(big_sum))
        self.wait(5)