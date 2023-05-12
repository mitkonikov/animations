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

        shifts = [LEFT * 3.5, LEFT * 2.5, LEFT * 0.8, RIGHT * 1.2, RIGHT * 3.2, RIGHT * 3.6]
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
        self.wait(3)

        id = [0, 3]
        for i in id:
            self.play(FadeOut(imgs[i]), run_time = 0.2)
            dots[i].set_opacity(0.4) 

        self.wait(3)
        xk = MathTex('x_k').scale(0.6).move_to(dots[1][1])
        xk1 = MathTex(r'x_{k+1}').scale(0.6).move_to(dots[2][1])
        self.play(self.camera.frame.animate.scale(0.7).shift(RIGHT * 0.1), Transform(dots[1][1], xk), Transform(dots[2][1], xk1))

        self.wait(5)

        self.play(*list(map(DrawBorderThenFill, x_dot_group)))
        self.play(x_dot_group.animate.shift(RIGHT * 1.2), run_time = 0.7)
        self.play(x_dot_group.animate.shift(RIGHT * 0.4), run_time = 0.3)
        self.play(x_dot_group.animate.shift(LEFT * 0.9), run_time = 0.5)
        self.wait(5)

        substrings = ['x_1', 'x_2', 'x_k', 'x_{k+1}', 'x_n', 'x']

        constants = r'- x_1 - x_2 - ... - x_k + x_{k+1} + ... + x_n'
        coeff = r'n - 2k'
        variable = r')x'

        f_k0 = MathTex(r'f(x) = \lvert x_1 - x \rvert  + \lvert x_2 - x \rvert  + ... + \lvert x_k - x \rvert  + \lvert x_{k+1} - x \rvert + ... + \lvert x_n - x \rvert', substrings_to_isolate=substrings).move_to(self.camera.frame_center).shift(DOWN * 0.73).scale(0.25)
        f_k = MathTex(r'f(x) = x - x_1 + x - x_2 + ... + x - x_k + x_{k+1} - x + ... + x_n - x', substrings_to_isolate=substrings).move_to(self.camera.frame_center).shift(DOWN * 0.9).scale(0.27)
        f_k_rearrange = MathTex(r'f(x) = - x_1 - x_2 - ... - x_k + x_{k+1} + ... + x_n - (n - 2k)x', substrings_to_isolate=[constants, variable, coeff]).move_to(self.camera.frame_center).shift(DOWN * 1.1).scale(0.27)
        self.play(Write(f_k0), run_time = 0.8)
        self.wait(4)
        self.play(Write(f_k))

        self.play(f_k0.get_parts_by_tex('x').animate.set_fill(RED), 
                *[f_k0.get_parts_by_tex(substring).animate.set_fill(WHITE) for substring in substrings[0:-1]])
        self.play(f_k.get_parts_by_tex('x').animate.set_fill(RED), 
                *[f_k.get_parts_by_tex(substring).animate.set_fill(WHITE) for substring in substrings[0:-1]])
        self.wait(5)
        self.play(Write(f_k_rearrange))
        self.play(Indicate(f_k_rearrange.get_part_by_tex(constants)), run_time = 1.6)
        # self.play(Indicate(f_k_rearrange.get_part_by_tex(variable)), run_time = 1.6)
        self.wait()
        self.play(Indicate(f_k_rearrange.get_part_by_tex(coeff)), run_time = 1.6)
        self.wait(3)
        self.play(FadeOut(f_k), FadeOut(f_k0), self.camera.frame.animate.shift(DOWN * 2))
        self.wait(10)