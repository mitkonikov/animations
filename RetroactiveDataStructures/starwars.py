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

class StarWars(Scene):
    def construct(self):
        path_images = [Image.open('./bigbang/' + img) for img in images]
        
        # Convert to np array
        path_images = map(lambda x: np.array(x), path_images)

        # Create ImageMobjects
        path_images = list(map(lambda x: ImageMobject(x), path_images))
        
        SHIFT_RIGHT = RIGHT * 1.3
        SHIFT_OFFSET = (SHIFT_RIGHT * (len(path_images) - 1)) / 2

        for i in range(len(path_images)):
            path_images[i].scale(0.3)
            path_images[i].shift(SHIFT_RIGHT * i - SHIFT_OFFSET)

        # Draw images
        self.wait(1)
        self.play(*list(map(FadeIn, path_images)))

        # Create a Text object
        starWars = Text("Star\nWars", font="BreezeSans", should_center=True)
        starWars.shift(-SHIFT_OFFSET + LEFT * 2)

        self.wait(2)