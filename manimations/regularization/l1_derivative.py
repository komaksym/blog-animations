from manim import *

config.background_color = WHITE  # or "#FFFFFF"


class L1_derivative(Scene):
    def construct(self):
        """Title"""
        txt1 = Text("Derivative w.r.t.", color=BLACK).scale(1)

        # LaTeX-style wᵢ
        wi = MathTex("w_i", color=BLACK).scale(1.4)

        # Remaining text
        txt2 = Text("in L1", color=BLACK).scale(1)

        # Group them together in one line
        label = VGroup(txt1, wi, txt2).arrange(RIGHT, buff=0.15)
        wi.shift(DOWN * 0.1)

        # Tex
        tex = MathTex(
            r"\frac{\partial R}{\partial w_i} = \lambda \cdot \operatorname{sign}(w_i)", color=BLACK
        ).scale(1.2)

        # Unrolled
        tex_unrolled = MathTex(
            r"\frac{\partial R}{\partial w_i} =\begin{cases}\lambda & \text{if } w_i > 0 \\-\lambda & \text{if } w_i < 0 \\\text{undefined (but subgradients exist)} & \text{if } w_i = 0\end{cases}",
            color=BLACK,
        ).scale(1.1)

        self.add(label.to_edge(UP, buff=1), tex)
        self.wait(3)
        self.play(Transform(tex, tex_unrolled), run_time=3)
        self.wait(10)
