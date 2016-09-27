from kivy.app import App
from kivy.clock import Clock
from pong_game import PongGame


class PongApp(App):
    def build(self):

        # Make the game
        game = PongGame()

        # All we need to do to start the game is to serve the ball
        game.serve_ball()

        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    PongApp().run()
