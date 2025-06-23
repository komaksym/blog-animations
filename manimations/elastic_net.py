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
            font_size=50, color="black", 
            substrings_to_isolate=["cost = loss\ term +", "\lambda\sum_{j=1}^{k}\left|w_{j}\right|"]
        )
        l1_formula.scale(0.7)
        self.add(l1_formula.to_edge(UP, buff=1))
    

        """L2"""
        # Title
        l2_title = Text("L2 Regularization", color="black")
        l2_title.scale(0.5)
        self.add(l2_title.to_edge(UP, buff=2.5))

        # Formula
        l2_formula = MathTex(r"cost = loss\ term + \lambda\sum_{j=1}^{k}w_{j}^{2}",
                              font_size=50, color="black", 
                              substrings_to_isolate=["", "cost = loss\ term +", "\lambda\sum_{j=1}^{k}w_{j}^{2}"])
        l2_formula.scale(0.7)
        self.add(l2_formula.to_edge(UP, buff=3))


        """Elastic Net"""
        # Title
        elastic_title = Text("Elastic Net Regularization", color="black")
        elastic_title.scale(0.7)
        self.play(Write(elastic_title.to_edge(UP, buff=4.5)), run_time=2)

        # Formula
        elastic_net = MathTex(r"cost = loss\ term + \lambda_{1}\sum_{j=1}^{k}\left|w_{j}\right| +\lambda_{2}\sum_{j=1}^{k}w_{j}^{2}",
                       color='black', substrings_to_isolate=["cost = loss\ term +", "\lambda_{1}\sum_{j=1}^{k}\left|w_{j}\right|", "\lambda_{2}\sum_{j=1}^{k}w_{j}^{2}"])
        elastic_net.to_edge(UP, buff=5.0)

        # Transformations
        self.play(Transform(l1_formula[0], elastic_net[0]), Transform(l2_formula[0], elastic_net[0]), run_time=3)
        self.play(Transform(l1_formula[1], elastic_net[1]), run_time=3)
        self.play(Transform(l2_formula[2], elastic_net[2]), run_time=3)

        elastic_net.scale(0.7)
        #self.play(Write(elastic_net)



        # Rectangle highlighting the regularization term
        #rectangle = Rectangle(color=ORANGE, fill_opacity=0, 
        #                      width=6.2, height=2.2, stroke_width=5)
        #rectangle.shift(RIGHT * 2.7)

        ## Render the rectangle
        #self.play(Create(rectangle, run_time=2.5))
        self.wait(10)