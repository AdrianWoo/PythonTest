import sys
import pygame
from bullet import Bullet
from alien import Alien


# 按键按下动作
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


# 按键抬起动作
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


# 响应鼠标和键盘事件
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        # 监听退出事件
        if event.type == pygame.QUIT:
            sys.exit()
        # 按键按下动作
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # 按键抬起动作
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 屏幕绘制可见
    pygame.display.flip()


# 子弹位置更新
def update_bullets(bullets):
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


# 子弹开火更新
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
