class Settings:
    """游戏的基本设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3
        # 子弹属性
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3
        
        # 外星人属性
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示向右移动，为-1 表示向左移动
        self.fleet_direction = 1
        
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """ 初始化随游戏而变化的量 """
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        
        self.fleet_direction = 1
        
    def increase_speed(self):
        """ 提高设置速度的值 """
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale

