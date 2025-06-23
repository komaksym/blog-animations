from manim import *

config.background_color = WHITE  # or "#FFFFFF"


class L1_Formula(Scene):
    def construct(self):
        # Title
        title = Text("L1 Regularization", color="black")
        title.scale(1.2)
        self.add(title.to_edge(UP, buff=1))

        # Formula
        tex = MathTex(
            r"cost = loss\ term + \lambda\sum_{j=1}^{k}\left|w_{j}\right|", font_size=50, color="black"
        )
        tex.scale(1.2)
        self.add(tex)

        # Rectangle highlighting the regularization term
        rectangle = Rectangle(color=ORANGE, fill_opacity=0, width=2.7, height=2.2, stroke_width=5)
        rectangle.shift(RIGHT * 2.7)

        # Render the rectangle
        self.play(Create(rectangle, run_time=2.5))
        self.wait(10)
