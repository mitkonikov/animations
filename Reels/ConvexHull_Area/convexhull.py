from manim import *

class ConvexHull(Scene):
    def construct(self):
        points = [[-1, -1.2], [1.4, -1.4], [2.3, -0.4], [3, 1.8], [1, 2.3], [-0.3, 2], [-1.4, 1]]
        offset = [-0.5, -0.5]
        N = len(points)
        for i in range(N):
            points[i][0] += offset[0]
            points[i][1] += offset[1]
        
        def getLocation(point):
            return point[0] * RIGHT + point[1] * UP
        
        for point in points:
            p = Dot(getLocation(point), radius = 0.08, color = BLUE)
            self.play(DrawBorderThenFill(p), run_time = 0.3)

        # If you have a convex polygon
        poly = Polygon(*list(map(getLocation, points)))
        self.play(Create(poly))

        self.wait(1)

        # How do you find the area of it?
        self.play(poly.animate.set_fill(opacity = 0.2))
        self.wait(1)
        self.play(poly.animate.set_fill(opacity = 0))
        self.wait(1)

        # Let p0 be some fixed point
        fixed = Dot(getLocation(points[0]), color = RED, radius = 0.1)
        self.play(Create(fixed))
        p0t = MathTex("p_0").move_to(fixed).shift(DOWN * 0.4 + LEFT * 0.4)
        self.play(Write(p0t))
        
        # We can now divide the polygon into triangles
        triangles = []
        for i in range(0, N - 2):
            p0 = getLocation(points[0])
            p1 = getLocation(points[i + 1])
            p2 = getLocation(points[i + 2])
            tri = Polygon(*[p0, p1, p2], color = RED, fill_opacity = 0.2)
            triangles.append(tri)
            self.play(DrawBorderThenFill(tri), run_time = 0.4)

        self.wait(1)
        
        # The area of each triangle, can be found by the length of the cross product of these two vectors
        for i in range(len(triangles) - 1, 0, -1):
            t = triangles[i]
            self.play(FadeOut(t), run_time = 0.2)

        def vec(p0, pi, pii, time):
            v1 = Arrow(getLocation(points[p0]), getLocation(points[pi]), buff = 0, stroke_width=3, max_tip_length_to_length_ratio=0.1)
            v2 = Arrow(getLocation(points[p0]), getLocation(points[pii]), buff = 0, stroke_width=3, max_tip_length_to_length_ratio=0.08)
            v1t = MathTex("\\vec{v}", font_size = 32).move_to(v1, UP).shift(UP * 0.25 + RIGHT * 0.4)
            v2t = MathTex("\\vec{u}", font_size = 32).move_to(v2, UP)

            self.play(*[Create(v1), Write(v1t)], run_time = 1)
            self.play(*[Create(v2), Write(v2t)], run_time = 1)
            return [v1, v2, v1t, v2t]

        vectors = vec(0, 1, 2, 1)
        self.wait(2)

        area = MathTex("2P = |\\vec{u}\\times\\vec{v}|").shift(DOWN * 2.5 + RIGHT * 0.5)
        self.play(Write(area))
        self.wait(2)
        
        self.play(FadeOut(area), FadeOut(triangles[0]))
        self.wait(2)

        # You sum up the area for all of the triangles
        self.play(*[FadeOut(x) for x in vectors])
        
        for i in range(2, N - 1):
            V = vec(0, i, i + 1, 0.2)
            p = Polygon(*[getLocation(points[0]), getLocation(points[i]), getLocation(points[i+1])], color = RED, fill_opacity = 0.2)
            self.play(FadeIn(p), run_time = 0.5)
            self.wait(0.5)
            V.extend(p)
            self.play(*[FadeOut(x) for x in V])

        # This algorithm works in O(N) where N is the number of points on the polygon
        t = MathTex("O(N)")
        self.play(Write(t))
        
        self.wait(2)

        self.play(*[FadeOut(p0t), FadeOut(fixed)])
        self.wait(2)
        return