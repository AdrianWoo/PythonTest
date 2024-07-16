import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.aliens = pygame.sprite.Group()

        self._creat_fleet()
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """
        开始游戏的主循环
        """
        while True:
            self._check_events()  # 事件检测
            self.ship.update()  # 飞船移动
            self._update_bullets()  # 子弹绘制
            self._update_screen()  # 屏幕绘制
            self._update_aliens()
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

    def _creat_fleet(self):
        """创建一个外星编队"""
        # 外星人的间距为外星人的宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (
            self.settings.screen_height - 3 * alien_height
        ):  # 循环高度 用来创建多排
            while current_x < (
                self.settings.screen_width - 2 * alien_width
            ):  # 循环宽度 用来创建多个
                self._creat_alien(current_x, current_y)
                current_x += 2 * alien_width
            # 添加一行外星人后，重置x值 并递补y值
            current_x = alien_width
            current_y += 2 * alien_height

    def _creat_alien(self, x_position, y_position):
        """创建一个外星人 并将其放在当前行中"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        """绘制屏幕"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets:
            bullet.draw_bullet()
        # 绘制船
        self.ship.blitme()
        # 绘制外星人
        self.aliens.draw(self.screen)
        # 绘制屏幕可见
        pygame.display.flip()

    def _update_bullets(self):
        """更新子弹的位置并删除已消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        # 检查是否有子弹击中了外星人
        # 如果有，就删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _update_aliens(self):
        """更新外星舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """在有外星人达到边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """整个外星舰队向下移动,并改变方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1  # 通过-1 改变移动方向


if __name__ == "__main__":
    # 创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()
