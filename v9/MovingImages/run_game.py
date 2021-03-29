# we need this line in order to import PyGame framework
import pygame
import color_const
import draw_moving_img as moving_img

if __name__ == '__main__':
    # initiates pygame, initializes all the modules required for PyGame
    pygame.init()

    # defining the main display
    # canvas that we will draw things on
    # returns the pygame.Surface object on which we will perform graphical operations on
    # (800, 600) is a tuple: width and height
    canvas = pygame.display.set_mode((475, 600))

    # define background color
    canvas.fill([255, 255, 255])

    # title of the window
    pygame.display.set_caption('Moving images')

    # game clock, track time within a game (used for FPS - frames per second)
    # (average human can see ~30FPS)
    clock = pygame.time.Clock()

    done = False

    # initial step positions
    x_boat = y_boat = 0

    # initial directions
    dx_boat = 5
    dy_boat = 5

    # Zadatak 02
    x_cloud = y_cloud = 0

    dx_cloud = -5
    # dy_cloud = 5

    while not done:

        # pygame.event.get() - empties the event queue
        for event in pygame.event.get():
            # pygame.QUIT - event that will be triggered when we click on the close button
            if event.type == pygame.QUIT:
                done = True

            # print(event)

        x_boat += dx_boat
        x_cloud += dx_cloud

        # Pokazni zadatak
        _, in_boundary, _ = moving_img.draw_boat(canvas, x_boat, y_boat)

        if not in_boundary:
            dx_boat = -dx_boat

        '''
        Zadatak 01
        in_boundary, check_collision = moving_img.draw_boat(canvas, x_boat, y_boat)
        if check_collision or y_boat > 0:
            y_boat += dy_boat
            dx_boat = 0
        elif not in_boundary:
            dx_boat = -dx_boat
        '''
        '''
        Zadatak 02

        in_boundary_cloud, in_boundary_boat, check_collision_boat = moving_img.draw_boat(canvas, x_boat, y_boat,
                                                                                         x_cloud, y_cloud)
        if check_collision_boat or y_boat > 0:
            y_boat += dy_boat
            dx_boat = 0
        elif not in_boundary_boat:
            dx_boat = -dx_boat

        if not in_boundary_cloud:
            x_cloud = 170
            y_cloud = 0
        '''
        # updates entire Surface
        pygame.display.flip()

        # method that is called once per frame, how many milliseconds have passed since the previous value
        clock.tick(30)

    pygame.quit()
    quit()