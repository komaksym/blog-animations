from manim import *

config.background_color = WHITE  # or "#FFFFFF"


class ElasticNetFormula(Scene):
    def construct(self):
        """L1"""
        # Title
        l1_title = Text("L1 Regularization", color="black")
        l1_title.scale(0.5)
        self.add(l1_title.to_edge(UP, buff=0.5))

        # Formula
        l1_formula = MathTex(
            r"cost = loss\ term + \lambda\sum_{j=1}^{k}\left|w_{j}\right|",
            font_size=50,
            color="black",
            substrings_to_isolate=["cost = loss\ term +", "\lambda\sum_{j=1}^{k}\left|w_{j}\right|"],
        )
        l1_formula.scale(0.7)
        self.add(l1_formula.to_edge(UP, buff=1))

        """L2"""
        # Title
        l2_title = Text("L2 Regularization", color="black")
        l2_title.scale(0.5)
        self.add(l2_title.to_edge(UP, buff=2.5))

        # Formula
        l2_formula = MathTex(
            r"cost = loss\ term + \lambda\sum_{j=1}^{k}w_{j}^{2}",
            font_size=50,
            color="black",
            substrings_to_isolate=["", "cost = loss\ term +", "\lambda\sum_{j=1}^{k}w_{j}^{2}"],
        )
        l2_formula.scale(0.7)
        self.add(l2_formula.to_edge(UP, buff=3))

        """Elastic Net"""
        # Title
        elastic_net_title = Text("Elastic Net Regularization", color="black")
        elastic_net_title.scale(0.7)
        self.play(Write(elastic_net_title.to_edge(UP, buff=4.5)), run_time=2)

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
        )
        elastic_net.to_edge(UP, buff=5.0).scale(0.7)

        # Transform L1 and L2 into Elastic Net
        self.play(
            Transform(l1_formula[0], elastic_net[0]), Transform(l2_formula[0], elastic_net[0]), run_time=2
        )
        self.play(Transform(l1_formula[1], elastic_net[1]), run_time=2)
        self.play(Transform(l2_formula[2], elastic_net[3]), run_time=2)

        # Adding elastic net
        self.add(elastic_net)

        # Remove L1 and L2
        self.play(FadeOut(l1_formula), FadeOut(l2_formula), FadeOut(l1_title), FadeOut(l2_title))

        # Reposition Elastic Net
        self.play(
            elastic_net_title.animate.to_edge(UP, buff=1).scale(1.2),
            elastic_net.animate.move_to(ORIGIN).scale(1.2), run_time=2
        )

        """Drawing braces highlighting L1 and L2 terms"""
        # Draw L1
        l1_brace = Brace(elastic_net[1], direction=DOWN, color=ORANGE)
        l1_brace_text = Text(
            "L1 Regularization",
            color=ORANGE,
            weight=BOLD
        ).scale(0.4)

        l1_brace_text.next_to(l1_brace, DOWN)
        self.play(GrowFromCenter(l1_brace), FadeIn(l1_brace_text))

        # Draw L2
        l2_brace = Brace(elastic_net[3], direction=DOWN, color=BLUE)
        l2_brace_text = Text(
            "L2 Regularization",
            color=BLUE,
            weight=BOLD,
        ).scale(0.4)

        l2_brace_text.next_to(l2_brace, DOWN)
        self.play(GrowFromCenter(l2_brace), FadeIn(l2_brace_text))

        self.wait(20)
