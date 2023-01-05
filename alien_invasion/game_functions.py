import sys
import pygame


# 按键按下动作
def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


# 按键抬起动作
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


# 响应鼠标和键盘事件
def check_events(ship):
    for event in pygame.event.get():
        # 监听退出事件
        if event.type == pygame.QUIT:
            sys.exit()
        # 按键按下动作
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        # 按键抬起动作
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 屏幕绘制可见
    pygame.display.flip()