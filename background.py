import pygame
import os


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the image, set class rectangle to that of the image
        image_location = os.path.join("assets", "shade_bg.jpg")  # Find the path of the player image
        self.image = pygame.image.load(image_location).convert_alpha()  # Load the image
        self.rect = self.image.get_rect()  # Get the rect of the image

        # Set the initial position of the player at (400, 600), just above a platform
        self.rect.x = 0
        self.rect.y = 0
