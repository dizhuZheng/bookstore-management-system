import pygame
from pygame.sprite import Sprite

class Rain(Sprite):

    def __init__(self, screen, rect_x, rect_bottom):
        """Create a bullet at the ship's current position"""
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 5)
        #create a bullet rect at(0,0) and then set correct position
        self.rect.center = (rect_x, rect_bottom)
        #store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        #alien bullet image
        self.color = (200, 200, 200)
        self.speed_factor = 5

    def update(self):
        """move the bullet up the screen"""
        #update the decimal position of the bullet
        self.y += self.speed_factor
        #update the rect position
        self.rect.y = self.y

    def draw(self):
        """draw the bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect, 5)
