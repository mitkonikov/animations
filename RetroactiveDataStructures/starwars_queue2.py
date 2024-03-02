from manim import *
import os
from PIL import Image

# Get all of the images
directory_path = './bigbang'
images = os.listdir(directory_path)

# Print the list of files
print("Images: ")
for image in images:
    print(image)

class ManimQueue(Group):
    def __init__(self, sz, **kwargs):
        super().__init__(**kwargs)
        self.list = []
        self.counter = 0
        self.sz = sz

    def queue(self, image):
        image.shift(self.sz * self.counter)
        self.add(image)
        self.list.append(image)
        self.counter += 1
        return FadeIn(image)

    def dequeue(self):
        img = self.list[0]
        self.remove(self.list[0])
        self.list.pop(0)
        self.counter -= 1
        yield ApplyMethod(self.shift, -self.sz)
        yield FadeOut(img)

# This scene breaks at time 9
class StarWarsQueue2(Scene):
    def construct(self):
        commands = [(1, 'Q', 'sheldon.png'),
                    (2, 'Q', 'amy.png'),
                    (3, 'Q', 'leonard.png'),
                    (4, 'D'),
                    (5, 'Q', 'penny.png'),
                    (8, 'D'),
                    (9, 'Q', 'howard.png'),
                    (10, 'Q', 'bernie.png'),
                    (11, 'D'),
                    (12, 'D'),
                    (13, 'D'),
                    (14, 'Q', 'raj.png'),
                    (15, 'D'),
                    (16, 'D')]
        
        times = [Text('Time: ' + str(com[0]), font='BreezeSans').scale(0.9).shift(UP * 2.5 + RIGHT * 3) for com in commands]
        
        # Load the images
        path_images = dict()
        for img in images:
            arr = np.array(Image.open('./bigbang/' + img))
            path_images[img] = ImageMobject(arr).scale(0.3).shift(LEFT * 4)
        
        mq = ManimQueue(RIGHT * 1.3)

        for i in range(len(commands)):
            if (commands[i][0] > 9):
                break

            # Change to the new time
            if i > 0:
                self.play(Transform(times[0], times[i]))
            else:
                self.play(Write(times[i]))

            if commands[i][1] == 'Q':
                # Queue
                self.play(mq.queue(path_images[commands[i][2]]))
            else:
                # Dequeue
                self.play(*mq.dequeue())

        self.wait(6)