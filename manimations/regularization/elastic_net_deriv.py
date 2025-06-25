from manim import *

config.background_color = WHITE  # or "#FFFFFF"


class El_net_derivative(Scene):
    def construct(self):
        """Title"""
        txt1 = Text("Derivative w.r.t.", color=BLACK).scale(0.8)

        # LaTeX-style wᵢ
        wi = MathTex("w_i", color=BLACK).scale(1.2)

        # Remaining text
        txt2 = Text("in Elastic Net", color=BLACK).scale(0.8)
        txt3 = Text("(", color=BLACK).scale(0.8)

        txt4 = Text("L1", color=ORANGE).scale(0.8)
        txt5 = Text("+", color=BLACK).scale(0.8)
        txt6 = Text("L2", color=BLUE).scale(0.8)
        txt7 = Text(")", color=BLACK).scale(0.8)

        # Group them together in one line
        label = VGroup(txt1, wi, txt2, txt3, txt4, txt5, txt6, txt7).arrange(
            RIGHT, buff=0.15
        )

        # Move the wi term to align \w the title
        wi.shift(DOWN * 0.1)

        # Formula
        expr = MathTex(
            r"\frac{\partial R(w)}{\partial w_i} =\begin{cases}{\lambda_1} + 2\lambda_2 w_i & \text{if } w_i > 0 \\-\lambda_1 + 2\lambda_2 w_i & \text{if } w_i < 0 \\\text{undefined (subgradient in } [-\lambda_1, \lambda_1]) + 2\lambda_2 w_i & \text{if } w_i = 0\end{cases}",
            color="black",
        ).scale(0.8)
        expr[0][15:17].set_color(ORANGE)
        expr[0][29:32].set_color(ORANGE)
        expr[0][44:75].set_color(ORANGE)

        expr[0][18:23].set_color(BLUE)
        expr[0][33:38].set_color(BLUE)
        expr[0][76:81].set_color(BLUE)

        # expr.set_color_by_tex("2\lambda_2 w_i", color=BLUE)
        # expr.set_color_by_tex("\lambda_1", color=ORANGE)
        # expr[4].set_color(ORANGE)
        # el_net_deriv_tex[:-1].set_color(ORANGE)
        # el_net_deriv_tex[-1].set_color(BLUE)

        self.add(label.to_edge(UP, buff=1), expr)


# class El_net_derivative(Scene):
# def construct(self):
# tex = MathTex(r"{{ a^2 }} + {{ b^2 }} = {{ c^2 }}", color=BLACK)
# tex[0].set_color(BLUE)
# tex[2].set_color(RED)
# self.add(tex)
