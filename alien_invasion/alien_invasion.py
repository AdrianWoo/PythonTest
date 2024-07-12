import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """
        初始化游戏并创建运行资源
        """
        pygame.init()

        self.clock = pygame.time.Clock()  # 创建一个时钟用来控制帧率
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # 主窗体增加一个船
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """
        开始游戏的主循环
        """
        while True:
            self._check_events()  # 事件检测
            self.ship.update()  # 飞船移动
            self._update_bullets()
            self._update_screen()  # 屏幕绘制
            # 按照每秒60次的速度运行此函数
            self.clock.tick(60)

    def _check_events(self):
        """监听鼠标和键盘事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """按键按下事件"""
        # 左右移动
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            # 创建子弹 允许小于数量的子弹创建
            if len(self.bullets) < self.settings.bullet_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        """按键抬起事件"""
        # 停止左右移动
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """绘制屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets:
            bullet.draw_bullet()
        # 绘制船
        self.ship.blitme()
        # 绘制屏幕可见
        pygame.display.flip()
        
    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()
        
         #删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)


if __name__ == "__main__":
    # 创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()
