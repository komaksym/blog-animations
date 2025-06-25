from manim import *

config.background_color = WHITE  # Set white background globally


class RegularizationUpdateRules(Scene):
    def construct(self):
        # Title
        title = Text("Update rules:", font_size=40, color=BLACK).to_edge(UP, buff=1)

        # Update rules as black math
        l1_rule = MathTex(
            r"\text{L1:} \quad w \leftarrow w - \lambda_1 \cdot \text{sign}(w)", color=BLACK
        ).scale(0.9)
        l2_rule = MathTex(r"\text{L2:} \quad w \leftarrow w - 2\lambda_2 \cdot w", color=BLACK).scale(0.9)
        elastic_rule = MathTex(
            r"\text{Elastic Net:} \quad w \leftarrow w - \left( \lambda_1 \cdot \text{sign}(w) + 2\lambda_2 \cdot w \right)",
            color=BLACK,
        ).scale(0.9)

        # Arrange vertically
        updates = VGroup(l1_rule, l2_rule, elastic_rule).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        updates.next_to(title, DOWN, buff=0.8)

        # Add to scene
        self.add(title, updates)
