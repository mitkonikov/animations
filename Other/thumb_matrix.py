from typing import List
from manim import *
from colors import CYAN

class HiScene(Scene):
    def construct(self):
        m4 = Matrix([[1, 0, 0, 0, 1], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 1, 1]], h_buff=0.8)
        mt = Text('Transition Matrix').move_to(m4).shift(DOWN * 2.8)
        self.play(FadeIn(m4), FadeIn(mt), run_time = 2)
        self.wait(5)