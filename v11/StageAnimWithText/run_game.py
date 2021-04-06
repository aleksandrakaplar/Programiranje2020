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

    load.load_images('sprites/png/', 'cat')
    # print(sprite_stages)

    # initial step positions
    x_sprite = y_sprite = 0

    # initial directions
    dx_sprite = 5
    dy_sprite = 0

    # horizon
    y_horizon = 250

    while not done:

        # pygame.event.get() - empties the event queue
        for event in pg.event.get():
            # pygame.QUIT - event that will be triggered when we click on the close button
            if event.type == pg.QUIT:
                done = True

            # print(event)

        x_sprite += dx_sprite
        y_sprite += dy_sprite

        '''
        01 Example: No movement
        '''
        # draw.new_frame_no_movement(canvas, width, height, y_horizon)
        # in_boundary = True
        '''
        02 Example: With movement
        '''
        # draw.new_frame_movement(canvas, width, height, y_horizon, x_sprite)
        # in_boundary = True
        '''
        03 Example: With movement and boundary check
        '''
        # in_boundary = draw.new_frame_movement2(canvas, width, height, y_horizon, x_sprite)
        '''
        04 Example: With movement, collision and boundary check
        '''
        # in_boundary, collision = draw.new_frame_movement3(canvas, width, height, y_horizon, x_sprite)
        # if collision:
        #    dx_sprite = 0


        # 01 Zadatak: Nakon sto udari u kamen i padne da nastavi da hoda
        in_boundary, collision = draw.new_frame_movement4(canvas, width, height, y_horizon, x_sprite)
        if collision:
            dx_sprite = 0
        elif dx_sprite == 0:
            dx_sprite = 5

        if not in_boundary:
            x_sprite = 0

        '''
        # 02 Zadatak: sprite skok kad stigne do kamena
        in_boundary, collision = draw.new_frame_movement5(canvas, width, height, y_horizon, x_sprite, y_sprite)
        if collision:
            dy_sprite = -5

        if abs(y_sprite) > y_horizon / 2:
            dy_sprite = -dy_sprite
        elif y_sprite > 0:
            dy_sprite = 0

        if not in_boundary:
            x_sprite = 0
            # 02 Zadatak: sprite skok kad stigne do kamena
            y_sprite = 0
        '''
        # updates entire Surface
        pg.display.flip()

        # method that is called once per frame, how many milliseconds have passed since the previous value
        clock.tick(20)

    pg.quit()
    quit()
