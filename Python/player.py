from math import pi, sin, cos, sqrt, pow
from pyglet.gl import *

GRAVITATIONAL_CONSTANT = 1
FLOOR_CEILING = 30

class Player:
    def __init__(self, pos_x, pos_y):
        self.initial_x = pos_x
        self.initial_y = pos_y
        self.score = 0
        self.set(pos_x, pos_y, 0, 0, 18, True)

    def set(self, pos_x, pos_y, vel_x, vel_y, radius, alive):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.radius = radius
        self.alive = alive

    def draw(self):
        # print('Drawing player')
        iterations = int(2 * self.radius * pi)
        s = sin(2 * pi / iterations)
        c = cos(2 * pi / iterations)

        dx, dy = self.radius, 0

        glColor3f(0.8, 0.8, 0)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(self.pos_x, self.pos_y)
        for i in range(iterations + 1):
            glVertex2f(self.pos_x + dx, self.pos_y + dy)
            dx, dy = (dx * c - dy * s), (dy * c + dx * s)
        glEnd()
        pass

    def reset(self):
        self.pos_x = self.initial_x
        self.pos_y = self.initial_y
        self.vel_x = 0
        self.vel_y = 0
        self.alive = True
        self.score = 0
        pass

    def move(self):
        self.pos_y += self.vel_y

        if self.vel_y - GRAVITATIONAL_CONSTANT >= -7:
            self.vel_y += -GRAVITATIONAL_CONSTANT
        else:
            self.vel_y = -7

        if not self.alive:
            self.reset()
        else:
            self.score += 1
        self.draw()
        pass

    def colliding(self, pipe):
        player = self
        # Colliding with floor
        if player.pos_y < player.radius + FLOOR_CEILING:
            return True

        radius = player.radius
        if (player.pos_x + radius > pipe.position
        and player.pos_x - radius < pipe.position + pipe.width):
            # print('Checking...')
            if (player.pos_y > pipe.safe_point_top - radius
            or player.pos_y < pipe.safe_point_bottom + radius):
                # print('!!!!!!!!!!Not Safe!!!!!!!!!!!!')
                return True
            else:
                # print('Safe')
                pass
        else:
            pass
        return False;
