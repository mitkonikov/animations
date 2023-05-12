from manim import *
from random import randint

def animate(self, N, nodes, edges, queries, radius, spacing, font_size, timing = 1):
    # Parents array
    p = [-1 for _ in range(1, N + 2)]
    for edge in edges:
        p[edge[1]] = edge[0]
    
    # Setup the graph
    layout_config = {"orientation": "down", "vertex_spacing": spacing}

    g = Graph(vertices=nodes, edges=edges, vertex_config={
                "radius": radius}, layout="tree", layout_config=layout_config, root_vertex=1)
    
    self.play(Create(g))

    # Random values for each node
    values = [None for _ in range(1, N + 2)]
    vals = [0 for _ in range(1, N + 2)]
    for u in range(1, N+1):
        vals[u] = randint(1, 10)
        val = Text(f"{vals[u]}", color = "#244734", font_size=font_size, weight="BOLD")
        val.move_to(g.vertices[u].get_center())
        values[u] = val

    self.wait(0.4)
    self.play(AnimationGroup(*[Write(v) for v in values[1:]]), run_time=1)
    self.wait(4)

    # Query Function animated
    def query(u, v):
        last_cu = None
        last_cv = None
        texts = []
        un = []
        SUM = 0
        while u != -1:
            if last_cu is None:
                last_cu = Circle(0.35 * spacing[0], color = BLUE).shift(g.vertices[u].get_center())
                last_cv = Circle(0.4 * spacing[0], color = RED).shift(g.vertices[v].get_center())
                self.play(*[DrawBorderThenFill(last_cu), DrawBorderThenFill(last_cv)], run_time=1)
            else:
                anims = [last_cu.animate.move_to(g.vertices[u].get_center()), last_cv.animate.move_to(g.vertices[v].get_center())]
                self.play(AnimationGroup(*anims), run_time = 1 * timing)

            center = g.vertices[u].get_center()
            SUM += vals[u] * vals[v]
            t = Text(f"{vals[u] * vals[v]}", color = WHITE, font_size = font_size).shift(center + LEFT * 0.6 * spacing[0] + UP * 0.5 * spacing[0])
            vu_copy = values[u].copy()
            vv_copy = values[v].copy()
            self.add(vu_copy, vv_copy)
            self.play(Transform(Group(vu_copy, vv_copy), t), run_time = 1 * timing)
            un.append(vu_copy)
            un.append(vv_copy)
            u = p[u]
            v = p[v]
            texts.append(t)
        g_texts = Group(*texts)
        s = Text(f"Sum = {SUM}", font_size = 28).shift(UP * 3 + LEFT * 3.5)
        self.play(Transform(g_texts, s), run_time = 1.2)
        self.wait(4)
        all = [last_cu, last_cv, s, g_texts]
        self.remove(*all)
        self.remove(*texts)
        self.remove(*un)
        return
    
    for q in queries:
        query(q[0], q[1])
        self.wait(2)

    return (g, values, vals)

class Tree(Scene):
    def construct(self):
        # Setup the tree
        N = 32
        nodes = [i for i in range(1, N+1)]
        edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (3, 8), (4, 9), (4, 10), (4, 11), (5, 12), (5, 13), (5, 14), (6, 15), (8, 16), (9, 17),
                 (12, 18), (12, 19), (13, 20), (16, 21), (16, 22), (17, 23), (17, 24), (19, 25), (19, 26), (21, 27), (21, 28), (22, 29), (23, 30), (24, 31), (24, 32)]
        
        animate(self, N, nodes, edges, [[27, 29], [19, 24]], 0.3, [1, 1], 20)
        self.wait(2)

class TreeLong(Scene):
    def construct(self):
        # Setup the tree
        N = 30
        nodes = [i for i in range(1, N+1)]
        edges = []
        K = 8
        M = 20
        for i in range(2, K):
            edges.append((i - 1, i))
        edges.append((K - 1, K))
        edges.append((K - 1, M))
        for i in range(K + 1, M):
            edges.append((i - 1, i))
        for i in range(M + 1, N + 1):
            edges.append((i - 1, i))
        
        animate(self, N, nodes, edges, [[M - 2, N]], 0.1, [0.3, 0.3], 10, timing=0.2)
        self.wait(2)
        
class TreeBigLayer(Scene):
    def construct(self):
        # Setup the tree
        N = 32
        nodes = [i for i in range(1, N+1)]
        edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (3, 8), (4, 9), (4, 10), (4, 11), (5, 12), (5, 13), (5, 14), (6, 15), (8, 16), (9, 17),
                 (12, 18), (12, 19), (13, 20), (16, 21), (16, 22), (17, 23), (17, 24), (19, 25), (19, 26), (21, 27), (21, 28), (22, 29), (23, 30), (24, 31), (24, 32)]
        
        g, values, vals = animate(self, N, nodes, edges, [], 0.3, [1, 1], 20)
        
        levels = [[] for _ in range(10)]
        root = 1
        
        def dfs(i, level):
            levels[level].append(i)
            for edge in edges:
                if edge[0] == i:
                    dfs(edge[1], level + 1)

        dfs(root, 0)

        for l in levels:
            l.reverse()

        for u in levels[2]:
            self.play(g.vertices[u].animate.set_fill(color = RED), run_time = 0.5)

        self.wait(2)
        for i in range(len(levels[2])):
            for j in range(i + 1, len(levels[2])):
                ci = Circle(0.4, color = BLUE).move_to(g.vertices[levels[2][i]])
                cj = Circle(0.4, color = BLUE).move_to(g.vertices[levels[2][j]])
                self.play(*[DrawBorderThenFill(ci), DrawBorderThenFill(cj)], run_time=0.1)
                self.wait(0.1)
                self.play(*[FadeOut(ci), FadeOut(cj)], run_time=0.1)

class TreeRandom(Scene):
    def construct(self):
        # Setup the tree
        N = 50
        nodes = [i for i in range(1, N+1)]
        edges = []
        def w(m, iter):
            r = randint(1, m - 1)
            for _ in range(iter):
                r = max(r, randint(1, m - 1))
            return r

        for i in range(2, N + 1):
            edges.append((w(i, 2), i))

        g, values, vals = animate(self, N, nodes, edges, [], 0.2, [0.5, 0.6], 14, timing=0.2)
        self.wait(2)
        
        # Get the levels
        L = 20
        levels = [[] for _ in range(L)]
        root = 1
        
        def dfs(i, level):
            levels[level].append(i)
            for edge in edges:
                if edge[0] == i:
                    dfs(edge[1], level + 1)

        dfs(root, 0)

        colors = ["#1de051", "#0eecf0", "#f09956", "#56f0cf", "#0eecf0"]

        c = 0
        cc = 0
        for i in range(L):
            if len(levels[i]) == 0:
                break
            
            if c == 2:
                c = 0
                cc += 1

            # color the level
            for nn in range(len(levels[i])):
                node = levels[i][nn]
                self.play(g.vertices[node].animate.set_color(color = colors[cc % len(colors)]), run_time = 0.1)

            c += 1