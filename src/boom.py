import pygame


class Boom(pygame.sprite.Sprite):
    """
    爆炸
    """
    def __init__(self, windows, enemy, *groups):
        pygame.sprite.Sprite.__init__(self)
        self.boom1Img = "resources/images/boom_1_50.png"
        self.boom2Img = "resources/images/boom_2_50.png"
        self.boom1ImgCanvas = pygame.image.load(self.boom1Img)
        self.boom2ImgCanvas = pygame.image.load(self.boom2Img)
        # 死亡动画
        self.dieCartoon = []
        for i in range(0, 80):
            self.dieCartoon.append(1)
            self.dieCartoon.append(2)
        # 窗体
        self.windows = windows
        self.windowsRect = windows.get_rect()

        self.rect = enemy.rect
        self.enemy = enemy

    def update(self, *args):
        if len(self.dieCartoon) > 0:
            index = self.dieCartoon[0]
            if index == 1:
                self.windows.blit(self.boom1ImgCanvas, self.rect)
            elif index == 2:
                self.windows.blit(self.boom2ImgCanvas, self.rect)
            self.dieCartoon.pop(0)
            return False
        return True
