from manim import *

class MaxClique(Scene):
    def construct(self):
        self.vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.highlight_set = ['A','C','D','G','B']
        
        g = Graph(vertices=self.vertices, edges=[], layout="circular", vertex_config={"radius":0.25})
        self.play(DrawBorderThenFill(g))

        def rf(x):
            if x < 0.5:
                return 16 * x * x * x * x * x
            return 1 - pow(-2 * x + 2, 5) / 2

        for i in range(len(self.vertices)):
            mobjects = []
            for j in range(i+1, len(self.vertices)):
                mobjects.append(g._add_edge((self.vertices[i], self.vertices[j])))
            self.play(AnimationGroup(*(DrawBorderThenFill(m, rate_func=rf) for m in mobjects)), run_time = 0.5)

        for node in self.highlight_set:
            vertex = g.vertices[node]
            self.play(vertex.animate.set_color(WHITE), run_time = 0.01)

        for node in self.highlight_set:
            vertex = g.vertices[node]
            self.play(Indicate(vertex))

        self.wait(2)