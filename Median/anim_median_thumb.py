from typing import List
from manim import *
from colors import CYAN

class FuncDef(MovingCameraScene):
    def construct(self):
        number_line = NumberLine(
            x_range=[0, 10, 1],
            length=10,
            color=BLUE,
            include_tip=True,
            include_numbers=False,
            label_direction=DOWN,
        )

        self.play(DrawBorderThenFill(number_line))

        shifts = [LEFT * 3.5, LEFT * 2.5, LEFT * 0.8, RIGHT * 0.3, RIGHT * 3.2, RIGHT * 3.6]
        dots: List[Dot] = []
        imgs: List[ImageMobject] = []
        for i in range(len(shifts)):
            xi = VGroup()
            xi.add(Dot().shift(shifts[i]))
            xi.add(MathTex('x_' + str(i + 1)).scale(0.8).shift(shifts[i] + DOWN * 0.4))
            dots.append(xi)
            imgs.append(
                ImageMobject("./people/" + str(i + 1) + ".png").scale(0.15).shift(shifts[i]).shift(UP * 0.4)
            )

        x_dot = Dot(fill_color=RED).shift(shifts[1])
        x_dot_label = MathTex('x', fill_color=RED).scale(0.4).shift(shifts[1] + DOWN * 0.2)
        x_dot_group = VGroup()
        x_dot_group.add(x_dot, x_dot_label)

        for i in range(len(dots)):
            self.play(DrawBorderThenFill(dots[i]), FadeIn(imgs[i]), run_time = 0.4)

        self.wait(5)

        self.play(self.camera.frame.animate.scale(0.45).shift(LEFT * 1.7))

        self.play(*list(map(DrawBorderThenFill, x_dot_group)))
        self.play(x_dot_group.animate.shift(RIGHT * 0.2), run_time = 0.5)
        self.wait(5)

        self.wait(5)