from kivy.graphics import Rectangle
from kivy.properties import NumericProperty
from kivy.vector import Vector
from graphic_widget import GraphicWidget


class PongPaddle(GraphicWidget):

    GraphicClass = Rectangle

    # For Rectangle
    width = NumericProperty(10)
    height = NumericProperty(50)
    x = NumericProperty(0)
    y = NumericProperty(0)
    color_tuple = (0.5, 1, 1, 1)

    # Stuff we made
    score = 0

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.velocity_x = ball.velocity_x * -1
