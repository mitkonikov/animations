from manim import *
from Utils.colors import SAT_RED

class RoomScene(Scene):
    def construct(self):
        def rf(x):
            if x < 0.5:
                return 16 * x ** 5
            return 1 - pow(-2 * x + 2, 5) / 2
        
        room = SVGMobject('./MaxClique/Room.svg', height = 5.4, stroke_width=6)

        # Draw the room
        self.play(DrawBorderThenFill(room))
        self.wait(2)

        N = 8

        self.vertices = []
        for i in range(N):
            self.vertices.append(i)

        # Import the images
        images: ImageMobject = []
        for i in range(N):
            images.append(ImageMobject("./Utils/people/" + str((i%6)+1) + ".png").scale(0.25))

        # Create the graph
        g = Graph(vertices=self.vertices, edges=[], layout="circular", vertex_config={"radius":0.2}, edge_config={"stroke_width":4})
        
        # Move the images to each of the nodes
        for i in range(N):
            images[i].move_to(g.vertices[self.vertices[i]])

        # Animate the images
        self.play(*list(map(FadeIn, images)))
        self.wait(2)

        # Animate the graph
        g.z_index = -10
        for i in range(N):
            g.vertices[self.vertices[i]].z_index = -10
        self.play(DrawBorderThenFill(g))

        for i in range(len(self.vertices)):
            mobjects = []
            for j in range(i+1, len(self.vertices)):
                mobjects.append(g._add_edge((self.vertices[i], self.vertices[j])))
            self.play(AnimationGroup(*(DrawBorderThenFill(m, rate_func=rf) for m in mobjects)), run_time = 0.5)

        self.wait(5)

        return