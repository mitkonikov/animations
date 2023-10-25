from ast import List
from manim import *
from random import randint

class ProblemE_5(Scene):
    def construct(self):
        self.will_remove = False
        self.N = 10
        # self.queries = [(6, 1.8), (9, 1.4), (10, 0.8), (19, 0.2), (8, 2), (13, 2.6), (17, 0.8), (14, 2.2), (15, 1.4), (13, 3.2)]
        self.queries = [(6, 1), (8, 0.8), (3, 1.1), (1, 2.0), (2, 0.65), (5, 0.35)]

        places = []
        place_int = []
        start = LEFT * 10 + DOWN * 3
        ratio = 2
        padding = RIGHT * 0.15
        coeff = RIGHT
        for i in range(self.N):
            places.append(Line((start + i * coeff + padding) / ratio, (start + (i + 1) * coeff - padding) / ratio))
            place_int.append(Text(f"{i}", font_size=15).move_to(places[i].get_center()).shift(DOWN * 0.25))

        def rf(x):
            if x < 0.5:
                return 16 * x * x * x * x * x
            return 1 - pow(-2 * x + 2, 5) / 2
        
        self.wait(1)
        self.play(AnimationGroup(*(Create(m, rate_func=rf) for m in places)), run_time = 1.3)
        self.play(AnimationGroup(*(Write(m, rate_func=rf) for m in place_int)), run_time = 1.3)

        self.wait(1)

        self.rects: List[Rectangle] = [None for _ in range(20)]
        self.query_text = None

        for q in range(len(self.queries)):
            X, H = self.queries[q]
            if not self.query_text is None:
                self.play(FadeOut(self.query_text), run_time=0.3)
            
            self.query_text = Text(f"build: ({X}, {int(H * 10 * 10)})", font_size=28)
            self.query_text.shift(UP * 2.5 + LEFT * 3)
            self.play(Write(self.query_text), run_time=0.6)

            rect = Rectangle(BLUE, height = 0.001, width=0.2, fill_opacity=1)
            rect.move_to(places[X], aligned_edge=DOWN)
            rect.shift(UP * 0.05)
            rect2 = rect.copy()
            rect2.stretch_to_fit_height(height = H)
            rect2.move_to(places[X], aligned_edge=DOWN)
            rect2.shift(UP * 0.05)
            self.add(rect)
            self.play(Transform(rect, rect2))
            if not self.rects[X] is None:
                # self.remove(self.rects[X][0])
                # self.remove(self.rects[X][1])
                self.rects[X] = None
            self.rects[X] = (rect, rect2)

            if not self.will_remove:
                continue

            for u in range(X - 1, 0, -1):
                if self.rects[u] is None:
                    continue
                if self.rects[u][0].height <= H:
                    # self.remove(self.rects[u][1])
                    self.play(self.rects[u][0].animate.set_opacity(0.1), run_time=0.7)
                    # self.remove(self.rects[u][0])
                    self.rects[u] = None
        
        self.play(FadeOut(self.query_text), run_time=0.3)
        self.wait(1)

        dots = []
        for i in range(self.N):
            if self.rects[i] is None:
                continue
            d = Dot()
            d.move_to(self.rects[i][1], aligned_edge=UP)
            d.shift(UP * 0.1)
            self.play(Create(d), run_time=0.4)
            dots.append(d)

        for i in range(len(dots) - 1):
            l = Line(dots[i].get_center(), dots[i+1].get_center())
            self.play(Create(l), run_time=0.4)

        self.wait(5)

