from manim import *

config.background_color = WHITE  # or "#FFFFFF"


class ElasticNetFormula(Scene):
    def construct(self):
        """Elastic Net"""
        # Title
        elastic_net_title = Text("Elastic Net Regularization", color="black").scale(1.2)

        # Formula
        elastic_net = MathTex(
            r"cost = loss\ term + \lambda_{1}\sum_{j=1}^{k}\left|w_{j}\right| +\lambda_{2}\sum_{j=1}^{k}w_{j}^{2}",
            substrings_to_isolate=[
                "cost = loss\ term +",
                "\lambda_{1}\sum_{j=1}^{k}\left|w_{j}\right|",
                " +",
                "\lambda_{2}\sum_{j=1}^{k}w_{j}^{2}",
            ],
            color="black",
        ).scale(1.2)

        self.add(elastic_net_title.to_edge(UP, buff=1), elastic_net)

        """Drawing braces highlighting L1 and L2 terms"""
        # Draw L1
        l1_brace = Brace(elastic_net[1], direction=DOWN, color=ORANGE)
        l1_brace_text = Text("L1 Regularization", color=ORANGE, weight=BOLD).scale(0.5)

        l1_brace_text.next_to(l1_brace, DOWN)
        self.play(GrowFromCenter(l1_brace), FadeIn(l1_brace_text), run_time=2)

        # Draw L2
        l2_brace = Brace(elastic_net[3], direction=DOWN, color=BLUE)
        l2_brace_text = Text(
            "L2 Regularization",
            color=BLUE,
            weight=BOLD,
        ).scale(0.5)

        l2_brace_text.next_to(l2_brace, DOWN)
        self.play(GrowFromCenter(l2_brace), FadeIn(l2_brace_text), run_time=2)

        self.wait(10)
