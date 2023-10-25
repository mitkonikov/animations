from typing import List
from manim import *
from colors import CYAN

class TextOnly(Scene):
    def construct(self):
        # big_sum = MathTex(r'\displaystyle \sum_{i=1}^{n} \; \lvert x_{i} - x \rvert').scale(1.5)
        # txt = MathTex(r'Q \leq 10^5').scale(2)
        # txt = MathTex(r'i < j : ask(i) \geq ask(j)').scale(1.1)
        # txt = MathTex(r'i < j : A_i > A_j').scale(1.1)
        # big_sum = MathTex(r'\displaystyle \max_{i=S}^{N} \; A_i').scale(1.1)
        txt = MathTex(r'T_1, T_2, T_3, T_4, T_5 ... T_q').scale(1.1)
        self.play(Write(txt), run_time=2)
        self.wait(8)