from manim import *


config.background_color = WHITE  # or "#FFFFFF"


class RegularizationSetup(Scene):
    def construct(self):
        title = Text("Example Setup", font_size=40, color=BLACK).to_edge(UP, buff=1)

        # Initial coefficient
        w_init = (
            MathTex(r"\text{Initial coefficient: } w = 0.5", color=BLACK)
            .scale(0.8)
            .next_to(title, DOWN, buff=1.5)
        )

        # Regularization strengths
        lambdas = (
            VGroup(
                MathTex(
                    r"\text{L1 strength:\ } \lambda_1 = 0.1 \quad", color=BLACK
                ).scale(0.8),
                MathTex(
                    r"\text{L2 strength:\ } \lambda_2 = 0.1 \quad", color=BLACK
                ).scale(0.8),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .next_to(w_init, DOWN, buff=0.6)
        )

        # Add all to scene
        self.add(title, w_init, lambdas)
