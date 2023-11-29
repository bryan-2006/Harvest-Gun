import sys
import os
import pygame
import time
import threading
import csv

from background import Background

from objs import Fruit
from objs import Bomb
from objs import Ammo

from mouse import Crosshair

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Global constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 575
FRAME_RATE = 30
SEC = 99

# Useful vars
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

my_font = pygame.font.SysFont('Comic Sans MS', 30)
end_game_font = pygame.font.SysFont('Comic Sans MS', 50)

# Keeping track
score = 0

highscore = "-/-"  # was going to make it but then didn't :(

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Harvest Gun')  # name of window
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0)) # hides default cursor

# Make and initialize for each class
background = Background()
backgrounds = pygame.sprite.Group()
background.add(backgrounds)


fruit = Fruit()
fruits = pygame.sprite.Group()
fruit.add(fruits)

bomb = Bomb()
bombs = pygame.sprite.Group()
bomb.add(bombs)

ammo_crate = Ammo()
ammo_crates = pygame.sprite.Group()
ammo_crate.add(ammo_crates)


def make_fruit():
  threading.Timer(.5, make_fruit).start()
  Fruit().add(fruits)


make_fruit()


def make_bomb():
  threading.Timer(1.3, make_bomb).start()
  Bomb().add(bombs)


make_bomb()


def make_ammo():
  threading.Timer(2, make_ammo).start()
  Ammo().add(ammo_crates)


make_ammo()

crosshair = Crosshair()
crosshairs = pygame.sprite.Group()
crosshair.add(crosshairs)


game_on = True

start = time.time()
gun_start = time.time()
ammo = 12


def game_end_screen(circumstance):
    if circumstance == "win":
        gamescreen = end_game_font.render("You won! Your score is: " + str(score) + "!", False, (255,255,255))
        screen.blit(gamescreen, (80, 500 / 2))
    elif circumstance == "explode":
        gamescreen = end_game_font.render("You exploded! Score: " + str(score) + "!", False, (255,255,255))
        screen.blit(gamescreen, (80, 500 / 2))
    elif circumstance == "noammo":
        gamescreen = end_game_font.render("You ran out of ammo! Your score is: " + str(score) + "!", False,
        (255,255,255))
        screen.blit(gamescreen, (70, 500 / 2))

# pygame.mixer.music.load("bg_music.mp3")
# pygame.mixer.music.set_volume(.5)
# pygame.mixer.music.play()

while game_on:
    """
    EVENTS section - how the code reacts when users do things
    """

    end = time.time()
    current_time = end - start

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()

    # Keyboard events
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:
        pass  # Replace this line
    if keys_pressed[pygame.K_LEFT]:
        pass  # Replace this line
    if keys_pressed[pygame.K_RIGHT]:
        pass  # Replace this line
    if keys_pressed[pygame.K_DOWN]:
        pass  # Replace this line
    if keys_pressed[pygame.K_ESCAPE]:
        game_on = False

    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the # (x, y) coordinate

    gun_end = time.time()

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        if ((gun_end - gun_start) >= .3) and ammo > 0:

            pygame.mixer.music.load("gun_shot.mp3")
            pygame.mixer.music.set_volume(.5)
            pygame.mixer.music.play()

            ammo -= 1

            for fruit in fruits:
                if pygame.sprite.collide_rect(crosshair, fruit):
                    fruit.kill()
                    pygame.mixer.music.load("point.wav")
                    pygame.mixer.music.play()
                    score += 1

            for bomb in bombs:
                if pygame.sprite.collide_rect(crosshair, bomb):
                    bomb.kill()
                    pygame.mixer.music.load("game_end.wav")
                    pygame.mixer.music.play()
                    game_end_screen("explode")
                    game_on = False

            for ammo_crate in ammo_crates:
                if pygame.sprite.collide_rect(crosshair, ammo_crate):
                    pygame.mixer.music.load("reload.wav")
                    pygame.mixer.music.play()
                    ammo_crate.kill()
                    ammo = 12

            gun_start = time.time()
    if mouse_buttons[2]:  # If right mouse pressed
        pass

    """
    UPDATE section - manipulate everything on the screen
    
    """

    # dont want stuff to crash :) so kill it off after exits out of view

    for fruit in fruits:
        fruit.update()
        if fruit.rect.y >= 600:
            fruit.kill()
    for bomb in bombs:
        bomb.update()
        if bomb.rect.y >= 600:
            bomb.kill()
    for ammo_crate in ammo_crates:
        ammo_crate.update()
        if ammo_crate.rect.y >= 600:
            ammo_crate.kill()

    crosshair.update(mouse_pos)

    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    # Draw
    backgrounds.draw(screen)
    fruits.draw(screen)

    ammo_crates.draw(screen)

    bombs.draw(screen)
    crosshairs.draw(screen)

    text_surface = my_font.render("Score: " + str(score), False, (255,255,255))
    screen.blit(text_surface, (10, 0))

    end = time.time()

    current_time = end - start

    rounded_time = round(current_time)

    timer = my_font.render("Time: " + str(SEC - rounded_time) + "s", False, (255,255,255))
    screen.blit(timer, (1024 - 140, 0))

    ammo_count = my_font.render("Ammo: " + str(ammo), False, (255,255,255))
    screen.blit(ammo_count, (1024 - 140, 520))

    highscoretxt = my_font.render("Highscore: " + str(highscore), False, (255,255,255))
    screen.blit(highscoretxt, (10, 520))

    # name for fun
    name = my_font.render("Harvest Gun by Bryan", False, (0, 0, 0))
    screen.blit(name, (360, 0))

    if current_time >= SEC:
        pygame.mixer.music.load("time_end.wav")
        pygame.mixer.music.play()
        game_end_screen("won")
        game_on = False

    if ammo <= 0:
        pygame.mixer.music.load("game_end.wav")
        pygame.mixer.music.play()
        game_end_screen("noammo")
        game_on = False

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second

