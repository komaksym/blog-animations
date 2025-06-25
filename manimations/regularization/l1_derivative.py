from manim import *

config.background_color = WHITE  # or "#FFFFFF"


class L1_derivative(Scene):
    def construct(self):
        """Title"""
        txt1 = Text("Derivative w.r.t.", color=BLACK).scale(0.8)

        # LaTeX-style wᵢ
        wi = MathTex("w_i", color=BLACK).scale(1.2)

        # Remaining text
        txt2 = Text("in L1", color=BLACK).scale(0.8)

        # Group them together in one line
        label = VGroup(txt1, wi, txt2).arrange(RIGHT, buff=0.15)
        wi.shift(DOWN * 0.1)

        # Formula
        l1_deriv_tex = MathTex(
            r"\frac{\partial R}{\partial w_i} =\begin{cases}\lambda & \text{if } w_i > 0 \\-\lambda & \text{if } w_i < 0 \\\text{undefined (but subgradients exist)} & \text{if } w_i = 0\end{cases}",
            color="black",
        ).scale(0.8)

        self.add(label.to_edge(UP, buff=1), l1_deriv_tex)
