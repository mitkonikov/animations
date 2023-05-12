from manim import *

class MaxClique(Scene):
    def construct(self):
        circle = Circle(radius=2)
        vertices = [circle.point_at_angle(i * TAU / 7) for i in range(7)]
        edges = [(i, j) for i in range(7) for j in range(i + 1, 7)]
        clique = [0, 1, 2, 3]
        non_clique = [4, 5, 6]
        nodes = VGroup(*[Dot(vertices[i], color=WHITE, radius=0.2) for i in range(7)])
        edges = VGroup(*[Line(vertices[i], vertices[j]) for i, j in edges])
        self.play(Create(nodes), Create(edges), run_time=3)
        self.wait()