#
#      ____   ____  ___    ____   __________       __   ________   _______    ________   ___  
#     /   /  /   / /   \  /    \ \   _____  \     /  / /  _____/  /  ___  \  /  _____/  /  /  
#    /   /  /   / /     \/  /\  \ \  \    |  |   /  / /  /       /  /  /  / /  /       /  /   
#   /   /__/   / /   /\____/  \  \ \  \___/  |  /  / /  /_____  /  /__/  / /  /_____  /  /____
#  /__________/ /___/          \__\ \_______/  /__/  \_______/ /________/  \_______/ /_______/ 
#

import pygame
import time
import math
pygame.init()

class SimRun(object):
    class SimVar:
        _displayw = 800
        _displayh = 400
        _green = (0, 255, 0)
        _blue  = (0, 0, 255)
        _red   = (255, 0, 0)
        _white = (255, 255, 255)
        _black = (0, 0, 0)
        _rect1 = pygame.Rect(300,100,100,100)
        _rect2 = pygame.Rect(300,100,100,100)


    _vars = SimVar()

    def __init__(self):
        self.window = pygame.display.set_mode((self._vars._displayw,self._vars._displayh))
        self.window.fill(self._vars._white)

        self.windowclock = pygame.time.Clock()

        self.DrawShapes()

    def DrawShapes(self):
        pygame.draw.circle(self.window, self._vars._red, (750,50), 25, 5)
        pygame.draw.rect(self.window, self._vars._black, (50,50,50,50))
        pygame.draw.rect(self.window, self._vars._black, (50,105,50,50))

        x = 50
        y = 50
        
        # Draw Front
        for i in range(4):
            for j in range(5):
                pygame.draw.rect(self.window, self._vars._black, (x,y,50,50)) 
                y = y + 55
                pygame.display.update()

            x = x + 55
            y = 50

        x = 350
        y = 50

        # Draw Back
        for i in range(4):
            for j in range(5):
                pygame.draw.rect(self.window, self._vars._black, (x,y,50,50)) 
                y = y + 55
                pygame.display.update()

            x = x + 55
            y = 50

            font = pygame.font.Font('freesansbold.ttf', 32)

        # Text : Front
        X = 325
        Y = 700
        text = font.render('Front', True,  self._vars._black,  self._vars._white)
        textRect = text.get_rect()
        textRect.center = (X // 2, Y // 2)
        self.window.blit(text,textRect)

        # Text : Back
        X = 900
        Y = 700
        text = font.render('Back', True,  self._vars._black,  self._vars._white)
        textRect = text.get_rect()
        textRect.center = (X // 2, Y // 2)
        self.window.blit(text,textRect)

    def ColorNode(self, tact, on_time, side):
    
        tact_num_row = math.ceil(tact/4)
        tact_num_col = tact%4

        if tact_num_col == 0:
            tact_num_col = 4

        # Default side is "F", "f"
        side_offset = 0

        if side == "F":
            side_offset = 0
        elif side == "B":
            side_offset = 300

        pygame.draw.rect(self.window, self._vars._red, (55*tact_num_col+side_offset,55*tact_num_row,40,40))
        pygame.display.update()

        time.sleep(on_time)
        
        pygame.draw.rect(self.window, self._vars._black, (55*tact_num_col+side_offset,55*tact_num_row,40,40))
        pygame.display.update()

        start = time.time()
        print("Start = ", start)

        # done = False
        # while not done:
            # stop = time.time()
            # print("stop = ", stop)

            # elapsed = stop - start
            # print("elapsed = ", elapsed)

            # if elapsed > on_time:
            #     done = True
            # else:
                
            #     pygame.draw.rect(self.window, self._vars._red, (55*tact_num_col+side_offset,55*tact_num_row,40,40))
            #     pygame.display.update()
            #     time.sleep(0.5)
            #     pygame.draw.rect(self.window, self._vars._black, (55*tact_num_col+side_offset,55*tact_num_row,40,40))
            #     pygame.display.update()


            


    def CycleNodes(self):
        for i in range(20):
            on_time = 0.25
            self.ColorNode(i+1, on_time,"B")


if __name__ == '__main__':
    sim_run = SimRun()
    sim_run.CycleNodes()
