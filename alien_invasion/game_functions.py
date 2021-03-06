import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    # 响应键盘鼠标
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # 按键
    if event.key == pygame.K_RIGHT:
        # 向右
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左
        ship.moving_left = True
    elif event.type == pygame.K_SPACE:
        # 创建一颗子弹,并将其加入数组里面
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    # 松开
    if event.key == pygame.K_RIGHT:
        # 向右
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹,并将其加入数组里面
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, bullets):
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()


def update_bullets(bullets):
    # 更新子弹位置
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))
