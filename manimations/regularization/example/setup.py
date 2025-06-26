from manim import *


config.background_color = WHITE  # or "#FFFFFF"


class RegularizationSetup(Scene):
    def construct(self):
        title = Text("Example Setup", color=BLACK).to_edge(UP, buff=1).scale(1.2)

        # Initial coefficient
        w_init = (
            MathTex(r"\text{Initial coefficient: } w = 0.5", color=BLACK)
            .scale(1.2)
            .next_to(title, DOWN, buff=1)
        )

        l1_strength = MathTex(r"\text{\textbf{L1} strength:\ }" 
                              r"\lambda_1 = 0.1 \quad", color=BLACK).scale(1.2)

        l2_strength = MathTex(r"\text{L2 strength:\ } \lambda_2 = 0.1 \quad", color=BLACK).scale(1.2)

        # Highlight names and their variables
        l1_strength[0][0:2].set_color(ORANGE)
        l1_strength[0][11:13].set_color(ORANGE)

        l2_strength[0][0:2].set_color(BLUE)
        l2_strength[0][11:13].set_color(BLUE)

        # Regularization strengths
        lambdas = (
            VGroup(
                l1_strength, l2_strength
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.6)
            .next_to(w_init, DOWN, buff=0.6)
        )

        # Add all to scene
        self.add(title, w_init, lambdas)
