
from typing import List
from manim import *

class AddSum(Scene):
    def construct(self):
        number_line = NumberLine(
            x_range=[0, 10, 1],
            length=10,
            color=BLUE,
            include_tip=True,
            include_numbers=True,
            label_direction=DOWN,
        )

        numbers = [1, 1.5, 2, 4, 5.6, 7]
        dict_numbers = dict()
        for num in numbers:
            dict_numbers[float(num)] = Tex(str(num))

        labels = number_line.add_labels(dict_numbers, direction=UP, buff=None, font_size=None, label_constructor=None)
        self.play(DrawBorderThenFill(labels), run_time = 0.2)

        number_line.add_ticks()

        for i in range(len(numbers)):
            new_dot = number_line.ticks.add(Dot().move_to(labels.number_to_point(numbers[i])))
        
        self.play(DrawBorderThenFill(new_dot), run_time = 0.2)

        images: List[ImageMobject] = []
        for i in range(len(numbers)):
            images.append(
                ImageMobject("./people/" + str(i + 1) + ".png").scale(0.15).move_to(labels.number_to_point(numbers[i])).shift(UP)
            )

        for image in images:
            self.play(FadeIn(image), run_time = 0.1)

        destination = Dot(fill_color = RED)
        arrow_destination = Arrow(start = ORIGIN, end = UP / 4, stroke_color = RED, max_stroke_width_to_length_ratio=10).shift(DOWN)
        label_destination = Tex("destination", font_size = 24, fill_color = RED).move_to(arrow_destination, DOWN).shift(DOWN * 0.3)
        self.play(DrawBorderThenFill(destination), run_time = 0.2)
        self.play(*list(map(DrawBorderThenFill, [arrow_destination, label_destination])), run_time = 0.2)

        destination_group = VGroup()
        destination_group.add(destination, arrow_destination, label_destination)
        self.play(destination_group.animate.shift(LEFT * 2), run_time = 0.5)
        # self.play(*[images[i].animate.move_to(destination).shift(UP) for i in range(0, len(images))], run_time = 2)
        self.wait(2)

        sum_string = ""
        for i in range(len(numbers)):
            if (i == len(numbers) - 1):
                sum_string += r'\lvert ' + str(numbers[i]) + r' - 3 \rvert'
            else:
                sum_string += r'\lvert ' + str(numbers[i]) + r' - 3 \rvert + '

        str_numbers = ["1", ".5", "2", "4", "5.6", "7"]

        sum = MathTex(
            sum_string + r' = 12.1', 
            substrings_to_isolate=str_numbers
        ).shift(DOWN * 2).scale(0.8)
        
        self.play(DrawBorderThenFill(sum))
        self.wait(2)

        new_images: List[ImageMobject] = []
        for i in range(6):
            new_images.append(
                ImageMobject("./people/" + str(i + 1) + ".png")
                    .scale(0.15).move_to(sum.get_part_by_tex(str_numbers[i])).shift(DOWN / 2))
        
        self.play(*list(map(FadeIn, new_images)), run_time=2)
        self.wait(2)
