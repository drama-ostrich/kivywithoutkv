from kivy.properties import NumericProperty
from kivy.graphics import Rectangle

from kivy.uix.widget import Widget

from graphic_widget import GraphicWidget
from pong_ball import PongBall
from pong_paddle import PongPaddle


class PongGame(GraphicWidget):

    GraphicClass = Rectangle
    color_tuple = (0.2, 0.2, 0.2, 1)

    def __init__(self):
        super(PongGame, self).__init__()

        self.ball = PongBall()
        self.add_widget(self.ball)

        self.player1 = PongPaddle()
        self.add_widget(self.player1)

        self.player2 = PongPaddle()
        self.player2.x = 790
        self.add_widget(self.player2)

    def serve_ball(self):

        self.ball.center = self.center
        self.ball.velocity_x = -3
        self.ball.velocity_y = 4

    def update(self, dt):
        for b in [self.ball]:
            b.move()

            # bounce of paddles
            self.player1.bounce_ball(b)
            self.player2.bounce_ball(b)

            # bounce ball off bottom or top
            if b.top > self.top:
                b.velocity_y = -4
            elif b.y < self.y:
                b.velocity_y = 4

            # went of to a side to score point?
            if b.x < self.x:
                self.player2.score += 1
                self.serve_ball()
            if b.x > self.width:
                self.player1.score += 1
                self.serve_ball()

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y
