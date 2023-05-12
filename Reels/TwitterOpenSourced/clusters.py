from manim import *
from random import randint

class Clusters(Scene):
    def construct(self):
        self.vertices = [x for x in range(0, 20)]
        
        g = Graph(vertices=self.vertices, edges=[], vertex_config={"radius":0.25})

        def rf(x):
            if x < 0.5:
                return 16 * x * x * x * x * x
            return 1 - pow(-2 * x + 2, 5) / 2
        
        # outside
        for i in range(0, 8):
            g.vertices[i].move_to(randint(-300, 300) / 100 * DOWN + randint(-300, 300) / 100 * RIGHT)
        for i in range(8, 12):
            g.vertices[i].move_to(randint(-800, -400) / 100 * DOWN + randint(200, 500) / 100 * RIGHT)
        for i in range(12, 16):
            g.vertices[i].move_to(randint(-800, -400) / 100 * DOWN + randint(-500, -200) / 100 * RIGHT)
        for i in range(16, 20):
            g.vertices[i].move_to(randint(400, 800) / 100 * DOWN + randint(-500, -200) / 100 * RIGHT)

        self.play(DrawBorderThenFill(g))
        
        mobjects = []
        for i in range(8):
            for j in range(i+1, 8):
                if randint(1, 100) <= 80:
                    mobjects.append(g._add_edge((self.vertices[i], self.vertices[j])))

        for i in range(len(self.vertices)):
            for j in range(i+1, len(self.vertices)):
                if i < 8 and j < 8:
                    continue
                v = g.vertices[i].get_center() - g.vertices[j].get_center()
                k = np.linalg.norm(v)
                p = 100 * (1 / ((k/2)**2))
                if randint(1, 100) <= p:
                    mobjects.append(g._add_edge((self.vertices[i], self.vertices[j]), edge_config={ "stroke_opacity": 0.3 }))
  
        self.play(AnimationGroup(*(DrawBorderThenFill(m, rate_func=rf) for m in mobjects)), run_time = 0.5)

        in_network = Circle(4, color=RED)
        self.play(Create(in_network))

        for i in range(8):
            vertex = g.vertices[i]
            self.play(vertex.animate.set_color(RED), run_time = 0.06)

        self.wait(2)

        for i in range(8, len(self.vertices)):
            vertex = g.vertices[i]
            self.play(vertex.animate.set_color(BLUE), run_time = 0.06)

        self.wait(2)