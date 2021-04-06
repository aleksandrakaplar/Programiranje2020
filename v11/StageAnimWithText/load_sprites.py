import os
import pygame as pg

image_width = 0
image_height = 0

# 0: Dead, 1: Idle, 2: Jump, 3: Run, 4: Walk
image_stages = ["Dead", "Fall", "Hurt", "Idle", "Jump", "Run", "Slide", "Walk"]
sprite_stages = {}


def load_images(path, name_of_sprite):
    global image_width
    image_width = 200
    global image_height
    image_height = 150
    name_of_file = path + name_of_sprite

    # list that contains sprite images
    images_sprite_dead = read_pictures(name_of_file, 'Dead')
    images_sprite_fall = read_pictures(name_of_file, 'Fall')
    images_sprite_hurt = read_pictures(name_of_file, 'Hurt')
    images_sprite_idle = read_pictures(name_of_file, 'Idle')
    images_sprite_jump = read_pictures(name_of_file, 'Jump')
    images_sprite_run = read_pictures(name_of_file, 'Run')
    images_sprite_slide = read_pictures(name_of_file, 'Slide')
    images_sprite_walk = read_pictures(name_of_file, 'Walk')

    # dictionary of sprite movements
    global sprite_stages
    sprite_stages = {0: images_sprite_dead, 1: images_sprite_fall, 2:images_sprite_hurt,
                     3: images_sprite_idle, 4: images_sprite_jump, 5: images_sprite_run,
                     6: images_sprite_slide, 7: images_sprite_walk}


def read_pictures(base_path, picture_name):
    images = []
    # list all files in directory
    for file_name in os.listdir(base_path):
        if os.path.isfile(os.path.join(base_path, file_name)):
            if picture_name in file_name:
                image = pg.image.load(os.path.join(base_path, file_name))
                image = pg.transform.scale(image, (image_width, image_height))
                images.append(image)

    return images


def get_index_sprite_by_name(sprite_name):
    return image_stages.index(sprite_name)
