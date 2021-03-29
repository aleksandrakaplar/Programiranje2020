# we need this line in order to import PyGame framework
import pygame as pg
import draw_sprites
import load_sprites as load
import draw_sprites as draw


# list all color values in Pygame
def load_predefined_colors():
    print(pg.color.THECOLORS)


if __name__ == '__main__':
    # initiates pygame, initializes all the modules required for PyGame
    pg.init()

    (width, height) = (1000, 500)
    canvas = pg.display.set_mode((width, height))

    # title of the window
    pg.display.set_caption('Stage Animation')

    # game clock, track time within a game (used for FPS - frames per second)
    # (average human can see ~30FPS)
    clock = pg.time.Clock()

    done = False

    load.load_images('../../sprites/v10/png/', 'dino')
    # print(dino_stages)

    # initial step positions
    x_dino = y_dino = 0

    # initial directions
    dx_dino = 5
    dy_dino = 0

    # horizon
    y_horizon = 250

    while not done:

        # pygame.event.get() - empties the event queue
        for event in pg.event.get():
            # pygame.QUIT - event that will be triggered when we click on the close button
            if event.type == pg.QUIT:
                done = True

            # print(event)

        x_dino += dx_dino
        y_dino += dy_dino

        '''
        01 Example: No movement
        '''
        draw.new_frame_no_movement(canvas, width, height, y_horizon)
        in_boundary = True
        '''
        02 Example: With movement
        '''
        # draw.new_frame_movement(canvas, width, height, y_horizon, x_dino)
        # in_boundary = True
        '''
        03 Example: With movement and boundary check
        '''
        # in_boundary = draw.new_frame_movement2(canvas, width, height, y_horizon, x_dino)
        # if not in_boundary:
        #    x_dino = 0

        '''
        04 Example: With movement, collision and boundary check
        '''
        # in_boundary, collision = draw.new_frame_movement3(canvas, width, height, y_horizon, x_dino)
        # if collision:
        #    dx_dino = 0

        if not in_boundary:
            x_dino = 0
            # 02 Zadatak: Dino skok kad stigne do kamena
            y_dino = 0

        # updates entire Surface
        pg.display.flip()

        # method that is called once per frame, how many milliseconds have passed since the previous value
        clock.tick(30)

    pg.quit()
    quit()
