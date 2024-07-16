from typing import Any
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """一个描述外星人的类"""

    def __init__(self, ai_game) -> None:
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图像并设置其rect 属性
        self.image = pygame.image.load(
            "E:/SourceCode/PythonTest/alien_invasion/images/alien.bmp"
        )
        self.rect = self.image.get_rect()
        # 每个外星人出现在屏幕的左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人精确的水平位置
        self.x = float(self.rect.x)
    def check_edges(self):
        """如果外星人位于屏幕边缘就返回True"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (
            self.rect.left <= 0
        )
        
    def update(self):
        """ 移动外星人"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

  
