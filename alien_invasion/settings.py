class Setting():
    # 设置类
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed_factor = 1.5

        # 子弹
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 子弹总数量
        self.bullet_allowed = 3
