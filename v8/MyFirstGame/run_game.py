# we need this line in order to import PyGame framework
import pygame
import color_const
import draw_examples as draw

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
    pygame.display.set_caption('My First Game')

    # game clock, track time within a game (used for FPS - frames per second)
    # (average human can see ~30FPS)
    clock = pygame.time.Clock()

    done = False

    # load image from file system and scale
    image = pygame.image.load(r'.\img\picture1.jpg')
    image = pygame.transform.scale(image, (300, 200))

    while not done:

        # pygame.event.get() - empties the event queue
        for event in pygame.event.get():
            # pygame.QUIT - event that will be triggered when we click on the close button
            if event.type == pygame.QUIT:
                done = True

            # print(event)

        # 1. arg: left, 2. arg: top, 3. arg: width, 4. arg: height
        # rectangle = pygame.Rect(50, 100, 100, 50)
        # 1 arg: surface, 2. arg: color, 3. arg: shape
        # pygame.draw.rect(canvas, (0, 0, 225), rectangle)

        # pygame.draw.polygon(canvas, color_const.RED, [(50, 100), (100, 50), (150, 100)], 0)

        # canvas.blit(image, (150, 250))

        # Prvi zadatak
        # draw.draw_candle(canvas)
        # Drugi zadatak
        # draw.draw_nature(canvas)
        # Treci zadatak
        # draw.draw_boat(canvas)

        # updates entire Surface if no argument is passed, we can update portions of the
        # the Surface if we pass an argument
        # pygame.display.update(rectangle)

        # updates entire Surface
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    quit()
