from manim import *
from random import randint

class RandomBigGraph(MovingCameraScene):
    def construct(self):
        self.vertices = []
        N = 150

        for i in range(N):
            self.vertices.append(i)

        g = Graph(vertices=self.vertices,
                  edges=[],
                  vertex_config={"radius":0.1,"color":GREEN},
                  layout="random",
                  layout_scale=10,
                  edge_config={"stroke_width":2,"stroke_opacity":0.7}
                )

        for i in range(N):
            for j in range(i + 1, N):
                r = randint(1, 100)
                if (r <= 4):
                    g._add_edge((self.vertices[i], self.vertices[j]))

        self.play(DrawBorderThenFill(g))

        self.play(self.camera.frame.animate.scale(1.5), run_time=4)

        self.wait(4)
        return