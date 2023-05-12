from manim import *
from random import randint

class SQRT_Array(Scene):
    def construct(self):
        N = 15
        A = [randint(1, 20) for _ in range(N)]
        A[6] = 2
        A[7] = 2
        A[8] = 6
        
        def rf(x):
            if x < 0.5:
                return 16 * x * x * x * x * x
            return 1 - pow(-2 * x + 2, 5) / 2
        
        array = []
        array_int = []
        start = LEFT * 12
        ratio = 2
        padding = RIGHT * 0.15
        coeff = RIGHT * 1.6

        def get_center(i):
            m1 = (start + i * coeff + padding) / ratio
            m2 = (start + (i + 1) * coeff - padding) / ratio
            return (m2 + m1) / 2

        for i in range(N):
            center = get_center(i)
            c = Circle(0.28, color=BLUE, stroke_width=2)
            c.move_to(center)
            array.append(c)
            array_int.append(Text(f"{A[i]}", font_size=22).move_to(center))

        for i in range(N):
            self.play(Write(array_int[i]), Create(array[i]), run_time=0.6)
        
        self.wait(3)

        RANGE = [4, 10]
        range_line = Line(get_center(RANGE[0]) + LEFT * 0.4, get_center(RANGE[1]) + RIGHT * 0.4).shift(DOWN * 0.5)
        self.play(Create(range_line))

        def indicate(RANGE):
            for i in range(RANGE[0], RANGE[1] + 1):
                self.play(array[i].animate.set_fill(RED, opacity=0.5), run_time=0.3, rate_func=rf)
            self.wait(5)
            for i in range(RANGE[0], RANGE[1] + 1):
                self.play(array[i].animate.set_fill(RED, opacity=0), run_time=0.1, rate_func=rf)
            self.wait(5)

        indicate([4, 10])

        dividers = []
        for i in range(4):
            between = (get_center(i * 3 + 2) + get_center(i * 3 + 3)) / 2
            l = Line(between + UP, between + DOWN, stroke_width=1)
            dividers.append(l)
            self.play(Create(l), run_time=0.6, rate_func=rf)

        self.wait(3)
        
        indicate([6, 8])
        return