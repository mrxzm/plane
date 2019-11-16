import os
import pygame
import random
from pygame.locals import *
from src.background import Background
from src.own import Own
from src.enemy import Enemy
from src.boom import Boom
from src.bullet import Bullet

if __name__ == '__main__':
    print('run game!')
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    # 窗体
    back = Background()
    # 自己
    own = Own(back.screen)
    # 炮弹 bibibi
    bullets = pygame.sprite.Group()
    # 敌人
    enemies = pygame.sprite.Group()
    # 火花
    hits = pygame.sprite.Group()

    while True:
        clock.tick(60)
        # 背景
        back.update()
        # 产生敌人兵团 调整随机数改变兵团数量
        if len(enemies) < 15:
            ran = random.randint(0, 100)
            if 0 < ran < 3:
                enemies.add(Enemy(back.screen))
        time = pygame.time.get_ticks()
        if (time % 8) == 0:
            bullets.add(Bullet(back.screen, own))

        # 按键
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                # 动
                elif event.key in own.direction.keys():
                    own.direction[event.key] = 6

            elif event.type == KEYUP:
                # 停
                if event.key in own.direction.keys():
                    own.direction[event.key] = 0
        own.update()
        bullets.update()
        enemies.update()
        hits.update()

        for enemy in enemies:
            if enemy.rect.top > back.rect.bottom - 50:
                enemies.remove(enemy)
        # 碰撞
        bulletEnemy = pygame.sprite.groupcollide(bullets, enemies, True, True)
        if len(bulletEnemy) != 0:
            for en in bulletEnemy:
                hits.add(Boom(back.screen, en))
        enemy = pygame.sprite.spritecollide(own, enemies, True)
        if len(enemy) != 0:
            hits.add(Boom(back.screen, enemy[0]))

        # flip
        pygame.display.update()







