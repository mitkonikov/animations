from manim import *
from random import randint
from Utils.colors import SAT_GREEN

class Theorem(Scene):
    def construct(self):
        def rf(x):
            if x < 0.5:
                return 16 * x ** 5
            return 1 - pow(-2 * x + 2, 5) / 2
        
        g_def = MathTex("G_{n, p}").scale(1.7)
        self.play(FadeIn(g_def, shift=UP/2), rate_func=rf)

        self.wait(2)

        mxclique = MathTex("|\\textrm{maxclique}(G_{n, \\frac{1}{2}})|")
        self.play(FadeOut(g_def, shift=UP/2), FadeIn(mxclique, shift=UP/2), rate_func=rf)

        self.wait(3)

        mxclique2 = MathTex("|\\textrm{maxclique}(G_{n, \\frac{1}{2}})| \\approx 2 \cdot (1 \\pm \\mathcal{O}(1)) \cdot \log_2(n)")
        self.play(FadeOut(mxclique, shift=UP/2), FadeIn(mxclique2, shift=UP/2), rate_func=rf)
        
        self.wait(4)
        return