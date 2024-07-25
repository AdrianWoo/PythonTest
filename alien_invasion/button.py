import pygame.font


class Button:
    """创建按钮的类"""

    def __init__(self, ai_game, msg):
        """初始化按钮的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # 设置按钮的其他属性

        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # 创建对象 使按钮居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 只创建一次
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """将 msg 渲染成图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) # 文本转换为图像
        self.msg_image_rect = self.msg_image.get_rect() # 存储图像 并让字体居中
        self.msg_image_rect.center = self.rect.center 
        
    def draw_button(self):
        """ 绘制按钮 """
        self.screen.fill(self.button_color,self.rect) # 绘制按钮的矩形
        self.screen.blit(self.msg_image, self.msg_image_rect) # 传递字的图像和图像位置
