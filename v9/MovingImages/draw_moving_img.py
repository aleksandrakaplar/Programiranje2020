import pygame
import color_const as colors


def draw_boat(canvas, x_boat, y_boat, x_cloud=0, y_cloud=0, x_cloud_init=345, y_cloud_init=45, x_boat_init=165,
              x_sail_pole_init1=260, x_sail_init2=375):
    canvas = pygame.display.set_mode((520, 415))
    canvas.fill(colors.WHITE)
    # sun
    pygame.draw.circle(canvas, color=colors.YELLOW, center=(110, 70), radius=40)

    # cloud
    cloud = pygame.Rect(x_cloud_init + x_cloud, y_cloud_init, 155, 55)
    pygame.draw.ellipse(canvas, color=colors.LIGHT_BLUE, rect=cloud)

    # boat
    boat = pygame.Rect(x_boat_init + x_boat, 215 + y_boat, 215, 65)
    pygame.draw.rect(canvas, color=colors.BROWN, rect=boat)
    # sail
    pygame.draw.polygon(canvas, color=colors.BLACK,
                        points=[(x_sail_pole_init1 + x_boat, 60 + y_boat), (x_sail_init2 + x_boat, 195 + y_boat),
                                (x_sail_pole_init1 + x_boat, 195 + y_boat)], width=5)
    # pole
    pygame.draw.line(canvas, color=colors.BLACK, start_pos=(x_sail_pole_init1 + x_boat, 60 + y_boat),
                     end_pos=(x_sail_pole_init1 + x_boat, 215 + y_boat), width=5)

    # rock
    pygame.draw.rect(canvas, color=colors.BLACK, rect=(0, 200, 100, 85), width=2)

    # water
    pygame.draw.rect(canvas, color=colors.DARK_BLUE, rect=(0, 280, 520, 135))

    return check_in_screen(x_cloud_init + x_cloud+155, y_cloud_init + y_cloud, x_max=700), \
           check_in_screen(x_boat_init + x_boat + 215, y_boat + 65, x_min=215, y_min=65), \
           check_collision(x_boat_init + x_boat, 100)


def check_collision(x_moving_object1, x_object2, y_moving_object1=0, y_object2=0):
    if x_moving_object1 <= x_object2:
        return True
    return False


def check_in_screen(x, y, x_max=520, y_max=415, x_min=0, y_min=0):
    if x < x_min or x > x_max:
        return False
    if y < y_min or y > y_max:
        return False
    return True
