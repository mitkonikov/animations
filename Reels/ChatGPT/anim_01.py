from manim import *

class MaxClique(Scene):
    def construct(self):
        self.vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.highlight_set = ['A','C','D','G','B']
        
        # Generate edges for a full maximum clique
        self.edges = []
        for i in range(len(self.vertices)):
            for j in range(i+1, len(self.vertices)):
                self.edges.append((self.vertices[i], self.vertices[j]))
        
        g = Graph(vertices=self.vertices, edges=self.edges, layout="circular", vertex_config={"radius":0.25})
        self.play(Create(g))

        for node in self.highlight_set:
            vertex = g.vertices[node]
            self.play(vertex.animate.set_color(YELLOW))
