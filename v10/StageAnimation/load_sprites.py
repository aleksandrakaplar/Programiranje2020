import os
import pygame as pg

image_width = 0
image_height = 0

# 0: Dead, 1: Idle, 2: Jump, 3: Run, 4: Walk
image_stages = ["Dead", "Idle", "Jump", "Run", "Walk"]
dino_stages = {}


def load_images(path, name_of_sprite):
    global image_width
    image_width = 200
    global image_height
    image_height = 150
    name_of_file = path + name_of_sprite

    # list that contains dino images
    images_dino_dead = read_pictures(name_of_file, 'Dead')
    images_dino_idle = read_pictures(name_of_file, 'Idle')
    images_dino_jump = read_pictures(name_of_file, 'Jump')
    images_dino_run = read_pictures(name_of_file, 'Run')
    images_dino_walk = read_pictures(name_of_file, 'Walk')

    # dictionary of dino movements
    global dino_stages
    dino_stages = {0: images_dino_dead, 1: images_dino_idle, 2: images_dino_jump, 3: images_dino_run,
                   4: images_dino_walk}


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
