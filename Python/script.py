from player import Player
from pipe import Pipe
import pyglet
import os
import neat
pyglet.options['debug_gl'] = False

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
PLAYER_RADIUS = 18
PLAYER_HEIGHT = 2 * PLAYER_RADIUS
PIPE_STARTING_POSITIONS = [600, 900, 1200]
POP_SIZE = 10

def main(config_file):
    config = neat.config.Config(neat.DefaultGenome,
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet,
                                neat.DefaultStagnation,
                                config_file)
    population = neat.Population(config)
    # winner = p.run(eval_genomes)
    players = initialize_players()
    dead_players = []
    pipes = [Pipe(PIPE_STARTING_POSITIONS[0], PLAYER_HEIGHT),
            Pipe(PIPE_STARTING_POSITIONS[1], PLAYER_HEIGHT),
            Pipe(PIPE_STARTING_POSITIONS[2], PLAYER_HEIGHT)]
    window = pyglet.window.Window(height = WINDOW_HEIGHT, width = WINDOW_WIDTH)
    pass

    def update(self):
        # Do i need to alter this to be my eval genomes?
        # Or do i need to make an entirely different method for eval genomes?
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
    players = []
    for _ in range(POP_SIZE):
        players.append(Player(200, 250))
    return players

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_file = os.path.join(local_dir, 'config-feedforward.txt')
    main(config_file)
