from player import Player
from pipe import Pipe
import pyglet

SPACE_BAR = 32
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
PLAYER_RADIUS = 18
PLAYER_HEIGHT = 2 * PLAYER_RADIUS
PIPE_STARTING_POSITIONS = [600, 900, 1200]

def main():
    player = Player(200, 250)
    pipes = [Pipe(600, PLAYER_HEIGHT),
            Pipe(900, PLAYER_HEIGHT),
            Pipe(1200, PLAYER_HEIGHT)]
    window = pyglet.window.Window(height = WINDOW_HEIGHT, width = WINDOW_WIDTH)
    pass

    def update(self):
        window.clear()
        draw_background()
        player.move()
        # player.draw()
        reset_game = False
        for pipe in pipes:
            pipe.move()

            if(pipe.position < -pipe.width):
                pipe.reset()

            if player.colliding(pipe):
                # reset_game = True
                pass

        if reset_game:
            player.reset()
            reset_pipes()

        draw_floor()
        draw_score()
        pass

    def draw_floor():
        quad = (('v2f',(0,              0,
                        0,              30,
                        WINDOW_WIDTH,   30,
                        WINDOW_WIDTH,   0)))

        pyglet.gl.glColor3f(0.4,0.3,0.2)
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, quad)
        pass

    def draw_background():
        quad = (('v2f',(0,              0,
                        0,              WINDOW_HEIGHT,
                        WINDOW_WIDTH,   WINDOW_HEIGHT,
                        WINDOW_WIDTH,   0)))

        pyglet.gl.glColor3f(0.3,0.4,0.8)
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, quad)
        pass

    def draw_score():
        label = pyglet.text.Label(f'Score: {player.score}',
                          font_name='Times New Roman',
                          font_size=20,
                          x = 100, y = WINDOW_HEIGHT - 20,
                          anchor_x='center', anchor_y='center')
        label.draw()
        pass

    def reset_pipes():
        pipes[0].position = PIPE_STARTING_POSITIONS[0]
        pipes[1].position = PIPE_STARTING_POSITIONS[1]
        pipes[2].position = PIPE_STARTING_POSITIONS[2]
        pass

    @window.event
    def on_key_press(button, modifiers):
        if button is SPACE_BAR:
            # print("JUMP")
            player.vel_y = 12
        pass

    pyglet.clock.schedule_interval(update, 0.01)
    pyglet.app.run()

if __name__ == '__main__':
    main()
