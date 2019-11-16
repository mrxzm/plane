import os
import pygame


class Own(pygame.sprite.Sprite):
    """
    自己飞机
    """

    def __init__(self, windows):
        pygame.sprite.Sprite.__init__(self)
        self.ownImg = "resources/images/own.png"
        self.ownImgCanvas = pygame.image.load(self.ownImg)
        self.direction = {pygame.K_w: 0, pygame.K_a: 0, pygame.K_s: 0, pygame.K_d: 0}
        self.rect = self.ownImgCanvas.get_rect()
        self.image = self.ownImgCanvas
        # 窗体
        self.windows = windows
        self.windowsRect = windows.get_rect()
        # 初始位置
        self.rect.bottom = self.windowsRect.bottom
        self.rect.centerx = self.windowsRect.centerx

    def update(self, *args):
        if self.windowsRect.top < self.rect.top:
            self.rect.top -= self.direction[pygame.K_w]
        if self.windowsRect.bottom - 50 > self.rect.top:
            self.rect.top += self.direction[pygame.K_s]
        if self.windowsRect.left - 25 < self.rect.left:
            self.rect.left -= self.direction[pygame.K_a]
        if self.windowsRect.right - 40 > self.rect.left:
            self.rect.left += self.direction[pygame.K_d]

        self.windows.blit(self.ownImgCanvas, self.rect)

