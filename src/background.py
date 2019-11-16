import os
import pygame


class Background:
    """
    背景窗口
    """
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 900), 0, 32)
        pygame.display.set_caption("飞机大战1.0 作者：mrxzm")
        self.rect = self.screen.get_rect()
        self.bgImg = "resources/images/bg.jpg"
        self.bgImgCanvas = pygame.image.load(self.bgImg).convert()

    def update(self):
        self.screen.blit(self.bgImgCanvas, (0, 0))
