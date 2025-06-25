from manim import *

class RegularizationUpdateTable(Scene):
    def construct(self):
        self.camera.background_color = WHITE  # White background

        title = Text("Coefficient Updates Over 5 Steps", font_size=36, color=BLACK).to_edge(UP)

        table_data = [
            ["Step", "L1", "L2", "Elastic Net"],
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
            element_to_mobject=lambda x: Text(str(x), color=BLACK, font_size=28)
        ).scale(0.8)

        table.next_to(title, DOWN)

        self.add(title, table)
