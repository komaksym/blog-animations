from manim import *

config.background_color = WHITE  # Set white background globally


class SubstitutedUpdateRulesExpanded(Scene):
    def construct(self):
        title = Text("Update rules with substituted values", font_size=40, color=BLACK).to_edge(UP, buff=1)

        l1_sub = MathTex(r"w \leftarrow 0.5 - 0.1 \cdot \text{sign}(w)", color=BLACK).scale(0.9)
        l2_sub = MathTex(r"w \leftarrow 0.5 - 2 \times 0.1 \times 0.5", color=BLACK).scale(0.9)
        elastic_sub = MathTex(
            r"w \leftarrow 0.5 - \left( 0.1 \cdot \text{sign}(w) + 2 \times 0.1 \times 0.5 \right)",
            color=BLACK,
        ).scale(0.9)

        updates = VGroup(l1_sub, l2_sub, elastic_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        updates.next_to(title, DOWN, buff=1)

        self.add(title, updates)
