import sys
import pygame
from settings import *
from ship import *
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Setting()

    screen = pygame.display.set_mode(

        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建储存子弹数组
    bulltes = Group()

    # 开始游戏的主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bulltes)
        # 更新坐标
        ship.update()
        gf.update_bullets(bulltes)
        # 绘制屏幕
        gf.update_screen(ai_settings, screen, ship, bulltes)


run_game()
