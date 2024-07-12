from typing import Any
import pygame
from pygame.sprite import  Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color
        # 首先创建个子弹在（0，0）创建一个子弹的矩形，然后再设置其正确的位置
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop
        # 使用浮点数存储子弹的位置
        self.y = float(self.rect.y)

    def update(self):
        """更新子弹位置"""
        # 更新子弹的准确位置
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
