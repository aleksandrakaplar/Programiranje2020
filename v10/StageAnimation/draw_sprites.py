import pygame as pg
import load_sprites as load

image_index = 0
image_stage = 4

rock_x = 400
rock_y = 0
rock_width = 50
rock_height = 50


def new_frame_no_movement(canvas, width, height, y_horizon):
    # calculate images to show
    # calculate_stage()
    calculate_show_image()

    draw_background(canvas, width, height, y_horizon)
    draw_dino(canvas, y_horizon)


def new_frame_movement(canvas, width, height, y_horizon, dino_step):
    # calculate images to show
    calculate_show_image()
    # calculate_stage()

    draw_background(canvas, width, height, y_horizon)
    draw_dino(canvas, y_horizon, dino_step)


def new_frame_movement2(canvas, width, height, y_horizon, dino_step):
    # calculate images to show
    calculate_show_image()
    # calculate_stage()

    draw_background(canvas, width, height, y_horizon)
    draw_dino(canvas, y_horizon, dino_step)

    return check_in_screen(dino_step, y_horizon - load.image_height, width, height)


def new_frame_movement3(canvas, width, height, y_horizon, dino_step):
    # check collision
    collision = check_collision(rock_x, dino_step + load.image_width/2)

    # calculate images to show
    continue_walking = calculate_stage(collision)
    calculate_show_image()

    draw_background(canvas, width, height, y_horizon)
    draw_dino(canvas, y_horizon, dino_step)

    return check_in_screen(dino_step, y_horizon - load.image_height, width, height), collision


# 01 Zadatak: Nakon sto udari u kamen i padne da nastavi da hoda
def new_frame_movement4(canvas, width, height, y_horizon, dino_step):
    # check collision
    collision = check_collision(rock_x, dino_step + load.image_width / 2)

    # calculate images to show
    continue_walking = calculate_stage(collision)
    calculate_show_image()

    if continue_walking is not None:
        dino_step += 3
        collision = check_collision(rock_x, dino_step + load.image_width / 2)

    draw_background(canvas, width, height, y_horizon)
    draw_dino(canvas, y_horizon, dino_step)

    return check_in_screen(dino_step, y_horizon - load.image_height, width, height), collision


# Zadatak 02: Nakon sto udari o kamen, treba da ga preskoci pa nastavi da hoda
def new_frame_movement4(canvas, width, height, y_horizon, dino_step_x, dino_step_y):
    # check collision
    collision = check_collision(rock_x, dino_step_x + load.image_width / 2)

    # calculate images to show
    continue_walking = calculate_stage2(collision, dino_step_y, y_horizon)
    calculate_show_image()

    draw_background(canvas, width, height, y_horizon)
    draw_dino(canvas, y_horizon, dino_step_x, dino_step_y)

    return check_in_screen(dino_step_x, y_horizon - load.image_height, width, height), collision


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
        image_stage = 0
        image_index = 0
    # 01 Zadatak: Nakon sto udari o kamen i padne da nastavi da hoda
    elif image_stage == 0 and image_index >= len(load.dino_stages.get(image_stage)) - 1:
        image_index = 0
        image_stage = 4
        return True


# Zadatak 02: Nakon sto udari o kamen, treba da ga preskoci pa nastavi da hoda
def calculate_stage2(collision, dino_y, y_horizon):
    global image_stage
    global image_index
    if collision and image_stage != 2:
        image_stage = 2
        image_index = 0
    # check when stage 2 (jump) is finished and old stage 4 (walk) starts again
    elif image_stage == 2 and dino_y > 0:
        image_index = 0
        image_stage = 4
        return True


def calculate_show_image():
    global image_index

    image_index += 1

    if image_index >= len(load.dino_stages.get(image_stage)):
        if image_stage == 0:
            image_index = len(load.dino_stages.get(image_stage)) - 1
        else:
            image_index = 0


def draw_background(canvas, width, height, y_horizon):
    canvas.fill(pg.Color("deepskyblue"))  # color of the background
    pg.draw.rect(canvas, color=pg.Color("navajowhite"),
                 rect=(0, y_horizon, width, height - y_horizon))  # draw the ground
    pg.draw.rect(canvas, color=pg.Color("navajowhite4"),
                 rect=(rock_x, y_horizon - rock_height, rock_width, rock_height))  # draw rock


def draw_dino(canvas, y_horizon, x_dino=0, y_dino=0):
    canvas.blit(load.dino_stages[image_stage][image_index], (x_dino, y_horizon - load.image_height + 15 + y_dino))
