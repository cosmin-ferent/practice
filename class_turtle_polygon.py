import turtle


class Polygon(object):
    def __init__(self, size, sides, name):
        self.size = size
        self.sides = sides
        self.turn_angle = 360 / self.sides
        self.name = name

    def draw(self):
        for _ in range(self.sides):
            turtle.forward(self.size)
            turtle.right(self.turn_angle)
        turtle.done()


triangle = Polygon(100, 3, 'Triangle')
square = Polygon(100, 4, 'Square')
pentagon = Polygon(100, 5, 'Pentagon')
hexagon = Polygon(100, 6, 'Hexagon')
circle = Polygon(1, 500, 'Circle')

triangle.draw()
