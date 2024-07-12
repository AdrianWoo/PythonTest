import sys
import pygame

class AlienInvasion:
    """管理游戏资源和行为的类
    """
    def __init__(self):
        '''
        初始化游戏并创建运行资源
        '''
        pygame.init()
        self.clock = pygame.time.Clock() # 创建一个时钟用来控制帧率
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Alien Invasion')
        # 设置一个背景颜色
        self.bg_color = (230,230,230)
    
    def run_game(self):
        '''
        开始游戏的主循环
        '''
        while True:
            # 监听鼠标键盘事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # 每次循环都重新绘制屏幕
            self.screen.fill(self.bg_color)
            # 绘制屏幕可见
            pygame.display.flip()
            # 按照每秒60次的速度运行此函数
            self.clock.tick(60) 
        

if __name__ == '__main__':
    # 创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()
    
                    
        