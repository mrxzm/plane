import os
import pygame
import random


class Enemy(pygame.sprite.Sprite):
    """
    敌机
    """
    def __init__(self, windows, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.enemyImg = "resources/images/enemy.png"
        self.enemyImgCanvas = pygame.image.load(self.enemyImg)

        self.rect = self.enemyImgCanvas.get_rect()
        self.image = self.enemyImgCanvas

        # 窗体
        self.windows = windows
        self.windowsRect = windows.get_rect()
        # 初始位置
        self.rect.top = self.windowsRect.top
        ran = random.randint(self.windowsRect.left, self.windowsRect.right - self.rect.right)
        self.rect.left = ran

    def update(self, *args):
        self.windows.blit(self.enemyImgCanvas, self.rect)
        self.rect.top += 1



