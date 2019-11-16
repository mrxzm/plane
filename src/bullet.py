import pygame


class Bullet(pygame.sprite.Sprite):
    """
    子弹
    """
    def __init__(self, windows, sprite, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.bulletImg = "resources/images/bullet.png"
        self.bulletImgCanvas = pygame.image.load(self.bulletImg)
        self.image = self.bulletImgCanvas
        self.rect = self.bulletImgCanvas.get_rect()
        self.speed = 10
        # 窗体
        self.windows = windows
        self.windowsRect = windows.get_rect()

        # 初始位置
        self.rect.top = sprite.rect.top

        self.rect.left = sprite.rect.left + 30

    def update(self, *args):
        self.rect.top -= self.speed
        self.windows.blit(self.bulletImgCanvas, self.rect)







