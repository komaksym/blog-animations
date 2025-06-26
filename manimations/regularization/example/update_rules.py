from manim import *

config.background_color = WHITE  # Set white background globally


class RegularizationUpdateRules(Scene):
    def construct(self):
        # Title
        title = Text("Update rules:", color=BLACK).scale(1.2).to_edge(UP, buff=1)

        # Update rules as black math
        l1_rule = MathTex(
            r"\text{L1:} \quad w \leftarrow w - \lambda_1 \cdot \text{sign}(w)", color=BLACK
        ).scale(1.2)

        l2_rule = MathTex(r"\text{L2:} \quad w \leftarrow w - 2\lambda_2 \cdot w", color=BLACK).scale(1.2)

        elastic_rule = MathTex(
            r"\text{Elastic Net:} \quad w \leftarrow w - \left( \lambda_1 \cdot \text{sign}(w) + 2\lambda_2 \cdot w \right)",
            color=BLACK,
        ).scale(1.2)

        # Highlight names
        l1_rule[0][0:3].set_color(ORANGE)
        l2_rule[0][0:3].set_color(BLUE)
        elastic_rule[0][0:10].set_color(PURPLE)

        # Arrange vertically
        updates = VGroup(l1_rule, l2_rule, elastic_rule).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        updates.next_to(title, DOWN, buff=1)

        # Add to scene
        self.add(title, updates)
