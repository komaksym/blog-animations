from manim import *

config.background_color = WHITE  # or "#FFFFFF"


class El_net_derivative(Scene):
    def construct(self):
        """Title"""
        txt1 = Text("Derivative w.r.t.", color=BLACK).scale(1)

        # LaTeX-style wᵢ
        wi = MathTex("w_i", color=BLACK).scale(1.4)

        # Remaining text
        txt2 = Text("in Elastic Net", color=BLACK).scale(1)
        txt3 = Text("(", color=BLACK).scale(1)

        txt4 = Text("L1", color=ORANGE).scale(1)
        txt5 = Text("+", color=BLACK).scale(1)
        txt6 = Text("L2", color=BLUE).scale(1)
        txt7 = Text(")", color=BLACK).scale(1)

        # Group them together in one line
        label = VGroup(txt1, wi, txt2, txt3, txt4, txt5, txt6, txt7).arrange(RIGHT, buff=0.15)

        # Move the wi term to align \w the title
        wi.shift(DOWN * 0.1)

        # Formula
        expr = MathTex(
            r"\frac{\partial R}{\partial w_i} =\begin{cases}"
            r"\boldsymbol{\lambda}_\textbf{1} + \textbf{2}\boldsymbol{\lambda}_\textbf{2} \mathbf{w_i} & \text{if } \mathbf{w}_i > 0 \\"
            r"\textbf{-}\boldsymbol{\lambda}_\textbf{1} + \textbf{2}\boldsymbol{\lambda}_\textbf{2} \mathbf{w_i} & \text{if } \mathbf{w}_i < 0 \\"
            r"\textbf{undefined (subgradient in } \textbf{[}\textbf{-}\boldsymbol{\lambda}_\textbf{1}, \boldsymbol{\lambda}_\textbf{1}\textbf{]}\textbf{)} + \textbf{2}\boldsymbol{\lambda}_\textbf{2}\mathbf{w}_\textbf{i} & \text{if } \mathbf{w}_i = 0"
            r"\end{cases}",
            color=BLACK
        ).scale(0.85)

        expr[0][12:14].set_color(ORANGE)
        expr[0][26:29].set_color(ORANGE)
        expr[0][41:72].set_color(ORANGE)

        expr[0][15:20].set_color(BLUE)
        expr[0][30:35].set_color(BLUE)
        expr[0][73:78].set_color(BLUE)

        self.add(label.to_edge(UP, buff=1), expr)
