import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class Star(Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.rawimage = pygame.image.load('star_22.bmp')
        self.image = self.rawimage
        self.rect = self.rawimage.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.centerx
        self.rect.y = self.rect.centery
        self.x = float(self.rect.x)
        self.speed = 2

    def rotate(self, degree):
        self.image = pygame.transform.rotate(self.rawimage, degree)
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.speed
        self.rect.x = self.x
