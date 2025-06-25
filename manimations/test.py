from manim import *

class ColorLegendExample(Scene):
    def construct(self):
        colors = [BLUE, RED, GREEN]
        labels = ["Circle", "Square", "Triangle"]
        legend_items = VGroup()
        for color, label in zip(colors, labels):
            shape = Square(side_length=0.5, fill_color=color, fill_opacity=1).next_to(legend_items, RIGHT, buff=0.2)
            text = Text(label).next_to(shape, RIGHT, buff=0.2)
            item = VGroup(shape, text)
            legend_items.add(item)

        legend = VGroup(*legend_items).arrange(DOWN, aligned_edge=LEFT)
        self.play(Create(legend))
        self.wait(2)