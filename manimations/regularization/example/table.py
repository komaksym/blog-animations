from manim import *

config.background_color = WHITE  # Set white background globally


class RegularizationUpdateTable(Scene):
    def construct(self):
        title = Text("Coefficient Updates Over 5 Steps", color=BLACK).scale(0.8).to_edge(UP, buff=0.3)

        table_data = [
            ["Step", r"\textbf{L1}", r"\textbf{L2}", r"\textbf{Elastic Net}"],
            ["0", "0.5", "0.5", "0.5"],
            ["1", "0.4", "0.4", "0.3"],
            ["2", "0.3", "0.32", "0.14"],
            ["3", "0.2", "0.256", "0.012"],
            ["4", "0.1", "0.2048", "-0.0904"],
            ["5", "0.0", "0.16384", "0.02768"],
        ]

        table = Table(
            table_data,
            include_outer_lines=True,
            line_config={"color": BLACK},
            element_to_mobject=lambda x: Tex(str(x), color=BLACK, font_size=28),
        ).scale(0.95)

        # Highlight
        table[0][1].set_color(ORANGE)
        table[0][2].set_color(BLUE)
        table[0][3].set_color(PURPLE)

        table.next_to(title, DOWN, buff=0.3)

        self.add(title, table)
