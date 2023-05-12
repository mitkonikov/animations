from manim import *

class PolishNotation(Scene):
    def construct(self):
        notation1 = MathTex('2 + 3').scale(1.5).shift(UP * 2)
        self.play(Write(notation1), run_time = 1.5)
        self.wait(2)

        notation2 = Tex('$2$ $3$ $+$').scale(1.5).move_to(notation1, DOWN).shift(DOWN)
        self.play(Write(notation2), run_time = 1.5)
        self.wait(1)
        
        notation21 = Tex('$5$').scale(1.5).move_to(notation2)
        self.play(Transform(notation2, notation21), run_time = 1.5)
        self.wait(2)

        notation3 = MathTex('5 + 3 * 4').scale(1.5).shift(DOWN)
        self.play(Write(notation3), run_time = 1.5)
        self.wait(2)

        notation4 = Tex('$5$ $3$ $4$ $*$ $+$').scale(1.5).move_to(notation3, DOWN).shift(DOWN)
        self.play(Write(notation4), run_time = 1.5)
        self.wait(2)

        notation41 = Tex('$5$ $12$ $+$').scale(1.5).move_to(notation4)
        self.play(Transform(notation4, notation41))
        self.wait(1)
        
        notation42 = Tex('$17$').scale(1.5).move_to(notation41)
        self.play(Transform(notation4, notation42))
        self.wait(1)