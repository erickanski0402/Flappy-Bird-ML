from player import Player
from pipe import Pipe
import pyglet
pyglet.options['debug_gl'] = False

SPACE_BAR = 32
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
PLAYER_RADIUS = 18
PLAYER_HEIGHT = 2 * PLAYER_RADIUS
PIPE_STARTING_POSITIONS = [600, 900, 1200]
POP_SIZE = 10

def main():
    players = initialize_players()
    dead_players = []
    pipes = [Pipe(600, PLAYER_HEIGHT),
            Pipe(900, PLAYER_HEIGHT),
            Pipe(1200, PLAYER_HEIGHT)]
    window = pyglet.window.Window(height = WINDOW_HEIGHT, width = WINDOW_WIDTH)
    pass

    def update(self):
        window.clear()
        draw_background()
        if players_alive() == 0:
            for player in players:
                player.reset()
            reset_pipes()

        for pipe in pipes:
            pipe.move()

            if(pipe.position < -pipe.width):
                pipe.reset()

        for player in players:
            player.move()
            # player.draw()

            for pipe in pipes:
                if player.colliding(pipe):
                    player.alive = False
                    break

        draw_floor()
        draw_score()
        draw_player_count()
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
        label = pyglet.text.Label(f'Score: {get_highest_score()}',
                          font_name='Times New Roman',
                          font_size=20,
                          x = 100, y = WINDOW_HEIGHT - 20,
                          anchor_x='center', anchor_y='center')
        label.draw()
        pass

    def draw_player_count():
        label = pyglet.text.Label(f'Players: {players_alive()}',
                          font_name='Times New Roman',
                          font_size=20,
                          x = 100, y = WINDOW_HEIGHT - 40,
                          anchor_x='center', anchor_y='center')
        label.draw()
        pass

    def reset_pipes():
        pipes[0].position = PIPE_STARTING_POSITIONS[0]
        pipes[1].position = PIPE_STARTING_POSITIONS[1]
        pipes[2].position = PIPE_STARTING_POSITIONS[2]
        pass

    def get_highest_score():
        score = 0
        for player in players:
            if player.score > score:
                score = player.score
        return score

    def players_alive():
        alive = []
        for player in players:
            if player.alive:
                alive.append(player)
        return len(alive)

    pyglet.clock.schedule_interval(update, 0.01)
    pyglet.app.run()

def initialize_players():
    print('ayyyy')
    players = []
    for _ in range(POP_SIZE):
        players.append(Player(200, 250))
    return players

if __name__ == '__main__':
    main()
