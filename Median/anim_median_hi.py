from typing import List
from manim import *
from colors import CYAN

class HiScene(Scene):
    def construct(self):
        hi = Text('Hi', font="Roboto Thin").scale(1.5)
        self.play(FadeIn(hi), run_time = 2)
        self.wait(5)