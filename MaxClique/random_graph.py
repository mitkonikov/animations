from manim import *
from random import randint
from Utils.colors import SAT_GREEN

class RandomSmallGraph(Scene):
    def construct(self):
        def rf(x):
            if x < 0.5:
                return 16 * x ** 5
            return 1 - pow(-2 * x + 2, 5) / 2
        
        self.vertices = []
        N = 10

        for i in range(N):
            self.vertices.append(i)

        g = Graph(vertices=self.vertices,
                  edges=[],
                  vertex_config={"radius":0.1,"color":SAT_GREEN},
                  layout="spring",
                  layout_config={"iterations":10},
                  edge_config={"stroke_width":2,"stroke_opacity":0.9}
                )

        self.play(DrawBorderThenFill(g))

        self.wait(3)

        u = randint(1, N) - 1
        v = randint(1, N) - 1
        uc = Circle(radius=0.2, color = None, stroke_width = 3, stroke_color = SAT_GREEN).move_to(g.vertices[self.vertices[u]])
        vc = Circle(radius=0.2, color = None, stroke_width = 3, stroke_color = SAT_GREEN).move_to(g.vertices[self.vertices[v]])

        self.play(*list(map(DrawBorderThenFill, [uc, vc])))

        g._add_edge((self.vertices[u], self.vertices[v]))

        self.wait(1)

        g._remove_edge((self.vertices[u], self.vertices[v]))

        self.play(*list(map(FadeOut, [uc, vc])))

        for i in range(N):
            for j in range(i + 1, N):
                r = randint(1, 100)
                if r <= 35:
                    g._add_edge((self.vertices[i], self.vertices[j]))

        er = Text("Erdős-Rényi model", color=SAT_GREEN).shift(DOWN * 2)
        self.play(g.animate.shift(UP), FadeIn(er, shift=UP/2), rate_func=rf)

        self.wait(4)
    
        g_def = MathTex("G_{n, p}").scale(1.7).shift(DOWN * 2)
        self.play(FadeOut(er, shift=UP/2), FadeIn(g_def, shift=UP/2), rate_func=rf)

        self.wait(4)
        return