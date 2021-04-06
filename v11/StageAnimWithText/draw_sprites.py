import pygame as pg
import load_sprites as load

# set sprite to run stage initially
image_index = 0
image_stage = 7

rock_x = 400
rock_y = 0
rock_width = 50
rock_height = 50

# initial stage
sprite_text = "Walk"


def new_frame_no_movement(canvas, width, height, y_horizon):
    # calculate images to show
    # calculate_stage()
    calculate_show_image()

    draw_background(canvas, width, height, y_horizon)
    draw_sprite(canvas, y_horizon)


def new_frame_movement(canvas, width, height, y_horizon, sprite_step):
    # calculate images to show
    calculate_show_image()
    # calculate_stage()

    draw_background(canvas, width, height, y_horizon)
    draw_sprite(canvas, y_horizon, sprite_step)


def new_frame_movement2(canvas, width, height, y_horizon, sprite_step):
    # calculate images to show
    calculate_show_image()
    # calculate_stage()

    draw_background(canvas, width, height, y_horizon)
    draw_sprite(canvas, y_horizon, sprite_step)

    return check_in_screen(sprite_step, y_horizon - load.image_height, width, height)


def new_frame_movement3(canvas, width, height, y_horizon, sprite_step):
    # check collision
    collision = check_collision(rock_x, sprite_step + load.image_width/2)

    # calculate images to show
    continue_walking = calculate_stage(collision)
    calculate_show_image()

    draw_background(canvas, width, height, y_horizon)
    draw_sprite(canvas, y_horizon, sprite_step)

    return check_in_screen(sprite_step, y_horizon - load.image_height, width, height), collision


# 01 Zadatak: Nakon sto udari u kamen i padne da nastavi da hoda
def new_frame_movement4(canvas, width, height, y_horizon, sprite_step):
    # check collision
    collision = check_collision(rock_x, sprite_step + load.image_width / 2)

    # calculate images to show
    continue_walking = calculate_stage(collision)
    calculate_show_image()

    if continue_walking is not None:
        sprite_step += 3
        collision = check_collision(rock_x, sprite_step + load.image_width / 2)

    draw_background(canvas, width, height, y_horizon)
    draw_sprite(canvas, y_horizon, sprite_step)

    return check_in_screen(sprite_step, y_horizon - load.image_height, width, height), collision


# Zadatak 02: Nakon sto udari o kamen, treba da ga preskoci pa nastavi da hoda
def new_frame_movement4(canvas, width, height, y_horizon, sprite_step_x, sprite_step_y):
    # check collision
    collision = check_collision(rock_x, sprite_step_x + load.image_width / 2)

    # calculate images to show
    continue_walking = calculate_stage2(collision, sprite_step_y, y_horizon)
    calculate_show_image()

    draw_background(canvas, width, height, y_horizon)
    draw_sprite(canvas, y_horizon, sprite_step_x, sprite_step_y)

    draw_text(canvas, width)

    return check_in_screen(sprite_step_x, y_horizon - load.image_height, width, height), collision


def check_in_screen(x, y, x_max, y_max, x_min=0, y_min=0):
    if x < x_min or x > x_max:
        return False
    if y < y_min or y > y_max:
        return False
    return True


def check_collision(x_moving_object1, x_object2, y_moving_object1=0, y_object2=0):
    if x_moving_object1 == x_object2 and image_stage != 0:
        return True
    return False


def calculate_stage(collision):
    global image_stage
    global image_index
    if collision and image_stage != 0:
        image_stage = load.get_index_sprite_by_name("Dead")
        image_index = 0
    # 01 Zadatak: Nakon sto udari o kamen i padne da nastavi da hoda
    elif image_stage == 0 and image_index >= len(load.sprite_stages.get(image_stage)) - 1:
        image_index = 0
        image_stage = load.get_index_sprite_by_name("Walk")
        return True


# Zadatak 02: Nakon sto udari o kamen, treba da ga preskoci pa nastavi da hoda
def calculate_stage2(collision, sprite_y, y_horizon):
    global image_stage
    global image_index
    global sprite_text

    if collision and image_stage != 4:
        sprite_text = "Jump"
        image_stage = load.get_index_sprite_by_name("Jump")
        image_index = 0
    # check when stage 4 (jump) is finished and old stage 7 (walk) starts again
    elif image_stage == 4 and sprite_y > 0:
        sprite_text = "Walk"
        image_index = 0
        image_stage = load.get_index_sprite_by_name("Walk")
        return True


def calculate_show_image():
    global image_index

    image_index += 1

    if image_index >= len(load.sprite_stages.get(image_stage)):
        if image_stage == 0 or image_stage == 4:
            image_index = len(load.sprite_stages.get(image_stage)) - 1
        else:
            image_index = 0


def draw_background(canvas, width, height, y_horizon):
    canvas.fill(pg.Color("deepskyblue"))  # color of the background
    pg.draw.rect(canvas, color=pg.Color("navajowhite"),
                 rect=(0, y_horizon, width, height - y_horizon))  # draw the ground
    pg.draw.rect(canvas, color=pg.Color("navajowhite4"),
                 rect=(rock_x, y_horizon - rock_height, rock_width, rock_height))  # draw rock


def draw_sprite(canvas, y_horizon, x_sprite=0, y_sprite=0):
    canvas.blit(load.sprite_stages[image_stage][image_index],
                (x_sprite, y_horizon - load.image_height + 15 + y_sprite))


def draw_text(canvas, width, height=0):
    # font for displaying the text
    font = pg.font.SysFont("Arial", 70)
    text_image = font.render(sprite_text, True, pg.Color("green"))
    x = (width - text_image.get_width()*2)
    y = text_image.get_height()

    canvas.blit(text_image, (x, y))
