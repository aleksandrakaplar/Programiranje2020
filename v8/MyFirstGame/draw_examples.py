import pygame
import color_const as colors


def draw_candle(canvas):
    canvas = pygame.display.set_mode((475, 600))
    canvas.fill(colors.WHITE)

    pygame.draw.line(canvas, color=colors.BLACK, start_pos=(216, 160), end_pos=(216, 175))

    candle = pygame.Rect(200, 175, 30, 115)
    pygame.draw.rect(canvas, color=colors.YELLOW, rect=candle)

    base = pygame.Rect(160, 290, 115, 30)
    pygame.draw.rect(canvas, color=colors.ORANGE, rect=base)

    # handle
    pygame.draw.circle(canvas, color=colors.ORANGE, center=(300,295), radius=25, width=10)


def draw_nature(canvas):
    canvas = pygame.display.set_mode((475, 600))
    canvas.fill(colors.WHITE)
    # sun
    pygame.draw.circle(canvas, color=colors.YELLOW, center=(77, 71), radius=40)

    # tree
    pygame.draw.polygon(canvas, color=colors.GREEN, points=[(160, 85), (100, 235), (220, 235)])

    # tree trunk
    trunk = pygame.Rect(153, 235, 20, 45)
    pygame.draw.rect(canvas, color=colors.BROWN, rect=trunk)

    # grass
    grass = pygame.Rect(0, 280, 475, 320)
    pygame.draw.rect(canvas, color=colors.GREEN, rect=grass)

    # mountain
    pygame.draw.polygon(canvas, color=colors.GREY, points=[(345, 133), (212, 280), (475, 280)])


def draw_boat(canvas):
    canvas = pygame.display.set_mode((520, 415))
    canvas.fill(colors.WHITE)
    # sun
    pygame.draw.circle(canvas, color=colors.YELLOW, center=(110, 70), radius=40)

    # cloud
    cloud = pygame.Rect(345, 45, 155, 55)
    pygame.draw.ellipse(canvas, color=colors.LIGHT_BLUE, rect=cloud)

    # boat
    boat = pygame.Rect(165, 215, 215, 65)
    pygame.draw.rect(canvas, color=colors.BROWN, rect=boat)

    # sail
    pygame.draw.polygon(canvas, color=colors.BLACK, points=[(260, 60), (375, 195), (260, 195)], width=5)
    # pole
    pygame.draw.line(canvas, color=colors.BLACK, start_pos=(260, 60), end_pos=(260, 215), width=5)

    # water
    pygame.draw.rect(canvas, color=colors.DARK_BLUE, rect=(0, 280, 520, 135))
