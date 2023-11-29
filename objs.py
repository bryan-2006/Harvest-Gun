import pygame
import os
import random


GRAVITY = 0.25
y_velocity = 1 * random.uniform(.01, .001)

point_obj_lst = ["squash.png", "pumpkin.png", "smol_pumpkin.png", "green_pumpkin.png"]

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the player image, set class rectangle to that of the image
        image_location = os.path.join("assets", random.choice(point_obj_lst))  # Find the path of the image
        self.image = pygame.image.load(image_location).convert_alpha()  # Load the image
        self.rect = self.image.get_rect()  # Get the rect of the image

        # Set the initial position/speed
        self.rect.y = random.randint(0, 100)
        self.y_speed = random.randrange(0, 1)  # Movement speed in the y direction
        side = ["left", "right"]
        if random.choice(side) == "left":
            self.rect.x = -105
            self.x_speed = random.randint(10, 20)  # Movement speed in the x direction
        else:
            self.rect.x = 1129
            self.x_speed = -1 * random.randint(10, 20)  # Movement speed in the x direction

    def fall(self):
        self.rect.x += self.x_speed
        self.y_speed += y_velocity  # Add velocity for the jump (must be greater than gravity to work properly)

    def update(self):
        self.fall()
        self.y_speed += GRAVITY  # Add gravity to y_speed
        self.rect.y += self.y_speed  # Add speed to position

        # End of updates


bomb_sprite_lst = ["tnt1.png", "tnt2.png", "tnt3.png"]


class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the player image, set class rectangle to that of the image
        image_location = os.path.join("assets", random.choice(bomb_sprite_lst))  # Find the path of the image
        self.image = pygame.image.load(image_location).convert_alpha()  # Load the image
        self.rect = self.image.get_rect()  # Get the rect of the image

        # Set the initial position/speed
        self.rect.y = random.randint(0, 100)
        self.y_speed = random.randrange(0, 15)  # Movement speed in the y direction
        side = ["left", "right"]
        if random.choice(side) == "left":
            self.rect.x = -105
            self.x_speed = random.randint(10, 20)  # Movement speed in the x direction
        else:
            self.rect.x = 1129
            self.x_speed = -1 * random.randint(10, 20)  # Movement speed in the x direction

    def fall(self):
        self.rect.x += self.x_speed
        self.y_speed += y_velocity  # Add velocity for the jump (must be greater than gravity to work properly)

    def update(self):
        self.fall()
        self.y_speed += GRAVITY  # Add gravity to y_speed
        self.rect.y += self.y_speed  # Add speed to position

        # End of updates


ammo_sprite_lst = ["ammo_def1.png", "ammo_def2.png"]


class Ammo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the player image, set class rectangle to that of the image
        image_location = os.path.join("assets", random.choice(ammo_sprite_lst))  # Find the path of the image
        self.image = pygame.image.load(image_location).convert_alpha()  # Load the image
        self.rect = self.image.get_rect()  # Get the rect of the image

        # Set the initial position/speed
        self.rect.y = random.randint(0, 100)
        self.y_speed = random.randrange(0, 15)  # Movement speed in the y direction
        side = ["left", "right"]
        if random.choice(side) == "left":
            self.rect.x = -105
            self.x_speed = random.randint(10, 20)  # Movement speed in the x direction
        else:
            self.rect.x = 1129
            self.x_speed = -1 * random.randint(10, 20)  # Movement speed in the x direction

    def fall(self):
        self.rect.x += self.x_speed
        self.y_speed += y_velocity  # Add velocity for the jump (must be greater than gravity to work properly)

    def update(self):
        self.fall()
        self.y_speed += GRAVITY  # Add gravity to y_speed
        self.rect.y += self.y_speed  # Add speed to position


        # End of updates
