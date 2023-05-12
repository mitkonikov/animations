from typing import List
from manim import *
from colors import CYAN

class FuncDef(MovingCameraScene):
    def construct(self):
        big_sum = MathTex(r'\displaystyle f(x) = \sum_{i=1}^{n} \; \lvert x_{i} - x \rvert', substrings_to_isolate=[r'x_{i}', 'x']).scale(1.2)
        self.play(DrawBorderThenFill(big_sum))
        self.wait(3)

        number_line_shift = DOWN
        
        number_line = NumberLine(
            x_range=[0, 10, 1],
            length=10,
            color=BLUE,
            include_tip=True,
            include_numbers=False,
            label_direction=DOWN,
        ).shift(number_line_shift)

        self.play(big_sum.animate.shift(UP), DrawBorderThenFill(number_line))
        
        shifts = [LEFT * 2.8, LEFT * 2.3, LEFT, RIGHT * 1.2, RIGHT * 3, RIGHT * 3.6]
        dots = []
        imgs = []
        for i in range(len(shifts)):
            xi = VGroup()
            xi.add(Dot().shift(number_line_shift + shifts[i]))
            xi.add(MathTex('x_' + str(i + 1)).scale(0.8).shift(number_line_shift + shifts[i] + DOWN * 0.4))
            dots.append(xi)
            imgs.append(
                ImageMobject("./people/" + str(i + 1) + ".png").scale(0.15).shift(number_line_shift + shifts[i]).shift(UP * 0.4)
            )

        for i in range(len(dots)):
            self.play(DrawBorderThenFill(dots[i]), FadeIn(imgs[i]), run_time = 0.4)

        self.wait(5)

        new_big_sum = big_sum.set_color_by_tex('x', RED)
        new_big_sum = big_sum.set_color_by_tex('x_{i}', WHITE)
        self.wait(5)
        