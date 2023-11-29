import pygame
import os


class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image_location = os.path.join("assets", "crosshair_v3.png")  # Find the path of the  image
        self.image = pygame.image.load(image_location).convert_alpha()  # Load the image
        self.rect = self.image.get_rect()  # Get the rect of the image

        # Set the initial position of the player at (400, 600), just above a platform
        self.rect.x = 400
        self.rect.y = 600

    def update(self, mouse_pos):

        teleport = True

        # End of EVENTS
        # UPDATES ------------------------------------

        # Check if we need to teleport
        if teleport:
            self.teleport(mouse_pos)  # if True, teleport to mouse position

    def collide_check_fruit(self, fruits):
        for fruit in fruits:
            if pygame.sprite.collide_rect(self, fruit):
                fruit.kill()

    def teleport(self, mousepos):
        x = mousepos[0]
        y = mousepos[1]
        self.rect.x = x - 15
        self.rect.y = y - 15
