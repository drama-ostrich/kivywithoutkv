from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class GraphicWidget(Widget):

    GraphicClass = Rectangle

    color_tuple = (1, 1, 1, 1)

    def __init__(self, **kwargs):
        super(GraphicWidget, self).__init__(**kwargs)

        with self.canvas:
            Color(*self.color_tuple)  # set the colour to red
            self.graphic = self.GraphicClass(pos=self.center, size=(self.width / 2., self.height / 2.))

        self.bind(pos=self.update_graphic, size=self.update_graphic)

    def update_graphic(self, *args):
        self.graphic.pos = self.pos
        self.graphic.size = self.size
