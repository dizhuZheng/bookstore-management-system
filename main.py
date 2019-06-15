import sys
from star import Star
import pygame
from pygame.sprite import Group
from rain import Rain

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('narue game')
    bg_color = (30, 30, 30)
    COUNT = pygame.USEREVENT + 1
    pygame.time.set_timer(COUNT, 1000)
    star = Star(screen)
    rains = Group()

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
                elif event.type == COUNT:
                    new_rain = Rain(screen, star.rect.centerx, star.rect.centery)
                    rains.add(new_rain)

            screen.fill(bg_color)
            star.blitme()
            star.update()
            for rain in rains:
                rain.update()
                rain.draw()

            pygame.display.flip()

run_game()
