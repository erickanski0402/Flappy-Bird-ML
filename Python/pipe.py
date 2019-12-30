from random import randrange
import pyglet

WINDOW_FLOOR = 0
WINDOW_CEILING = 500
PIPE_FLOOR = 35
RECT_CORNERS = 4
PIPE_CEILING = 350
RESET_POSITION = 850
# Height of safe point from bottom to top is 2.5h of player

class Pipe:
    def __init__(self, position, player_height):
        self.velocity = 2
        self.position = position
        self.player_height = player_height
        self.width = 1.5 * player_height
        self.safe_point_bottom = randrange(PIPE_FLOOR, PIPE_CEILING)
        self.safe_point_top = self.safe_point_bottom + (4 * player_height)
        self.past_window = False
        pass

    def draw(self):
        pos = self.position
        width = self.width
        bottom = self.safe_point_bottom
        top = self.safe_point_top
        quad_bottom = (('v2f', (pos, WINDOW_FLOOR,
                                pos + width, WINDOW_FLOOR,
                                pos + width, bottom,
                                pos, bottom)))

        quad_top = (('v2f', (pos, top,
                            pos + width, top,
                            pos + width, WINDOW_CEILING,
                            pos, WINDOW_CEILING)))

        pyglet.gl.glColor3f(0,0.7,0)
        pyglet.graphics.draw(RECT_CORNERS, pyglet.gl.GL_QUADS, quad_bottom)
        pyglet.graphics.draw(RECT_CORNERS, pyglet.gl.GL_QUADS, quad_top)
        pass

    def move(self):
        self.position += -self.velocity
        self.draw()
        pass

    def reset(self):
        self.safe_point_bottom = randrange(PIPE_FLOOR, PIPE_CEILING)
        self.safe_point_top = self.safe_point_bottom + (4 * self.player_height)
        self.position = RESET_POSITION
        pass
