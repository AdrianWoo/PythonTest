import pygame

import game_functions as gf
from Setting import Settings
from ship import Ship


def run_game():
    # 初始化游戏 并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        # 每次循环都重新绘制屏幕
        gf.update_screen(ai_settings, screen, ship)


run_game()