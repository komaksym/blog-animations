from manim import *

config.background_color = WHITE  # Set white background globally


class SubstitutedUpdateRulesExpanded(Scene):
    def construct(self):
        title = Text("Update rules with substituted values", color=BLACK).scale(1.2).to_edge(UP, buff=1)

        l1_sub = MathTex(r"\text{L1:} \quad w \leftarrow 0.5 - 0.1 \cdot \text{sign}(w)", color=BLACK).scale(1.2)
        l2_sub = MathTex(r"\text{L2:} \quad w \leftarrow 0.5 - 2 \times 0.1 \times 0.5", color=BLACK).scale(1.2)
        elastic_sub = MathTex(
            r"\text{Elastic Net:} \quad w \leftarrow 0.5 - \left( 0.1 \cdot \text{sign}(w) + 2 \times 0.1 \times 0.5 \right)",
            color=BLACK,
        ).scale(1)

        # Highlight names
        l1_sub[0][0:3].set_color(ORANGE)
        l2_sub[0][0:3].set_color(BLUE)
        elastic_sub[0][0:10].set_color(PURPLE)

        updates = VGroup(l1_sub, l2_sub, elastic_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        updates.next_to(title, DOWN, buff=1)

        self.add(title, updates)
