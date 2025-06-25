from manim import *

config.background_color = WHITE  # or "#FFFFFF"


class L1_derivative(Scene):
    def construct(self):
        """Title"""
        txt1 = Text("Derivative w.r.t.", color=BLACK).scale(0.8)

        # LaTeX-style wᵢ
        wi = MathTex("w_i", color=BLACK).scale(1.2)

        # Remaining text
        txt2 = Text("in L2", color=BLACK).scale(0.8)

        # Group them together in one line
        label = VGroup(txt1, wi, txt2).arrange(RIGHT, buff=0.15)
        wi.shift(DOWN * 0.1)

        # Formula
        l1_deriv_tex = MathTex(
            r"\frac{\partial R(w)}{\partial w_i} = 2\lambda w_i",
            color="black",
        ).scale(0.8)

        self.add(label.to_edge(UP, buff=1), l1_deriv_tex)
