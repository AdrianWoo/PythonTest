import sys
import pygame
from settings import Settings
from ship import Ship


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
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """
        开始游戏的主循环
        """
        while True:
            self._check_events()
            self._update_screen()
            # 按照每秒60次的速度运行此函数
            self.clock.tick(60)
    
    def _check_events(self):
        """ 监听鼠标和键盘事件 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        """ 绘制屏幕 """
        self.screen.fill(self.settings.bg_color)
        # 绘制船
        self.ship.blitme()
        # 绘制屏幕可见
        pygame.display.flip()
            



if __name__ == "__main__":
    # 创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()
