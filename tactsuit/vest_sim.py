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
import msvcrt

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

    def ColorNode(self, tact, side, on_time):
        
        # Converting seconds to milliseconds
        on_time = on_time*1000

        # time in millisecond from start program 
        start_time = pygame.time.get_ticks()
        current_time = pygame.time.get_ticks()

        # how long to show or hide
        delay = 50 # 50ms = 0.05s

        # time of next change 
        change_time = current_time + delay

        # Front tact : [1:20], Back tact [21:40]
        # if tact # > 20, assumed to be reffering to tact on back 
        if tact > 20:
            tact = tact - 20
            side = "B"
        elif tact > 40:
            print("ERROR:")
            print("ERROR:")
            print("ERROR: Tact number mus be between 1 - 40.")
            print("ERROR: Tact 01-20 refer to front or 'F' vest tacts.")
            print("ERROR: Tact 21-40 refer to back  or 'B' vest tacts.")
            print("ERROR:")
            print("ERROR:")
            pygame.quit()

        # Translating tact number to grid position
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
        
        show = True
        run = True
        while run:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - start_time

            # Checking if it is time to change
            if current_time >= change_time:
                # time for next change 
                change_time = current_time + delay
                show = not show

            # --- Drawing Squares ---
            if tact > 0:
                pygame.draw.rect(self.window, self._vars._black, (55*tact_num_col+side_offset,55*tact_num_row,40,40))
                if show:
                    pygame.draw.rect(self.window, self._vars._red, (55*tact_num_col+side_offset,55*tact_num_row,40,40))
            pygame.display.update()

            if elapsed_time > on_time:  
                if tact > 0:
                    pygame.draw.rect(self.window, self._vars._black, (55*tact_num_col+side_offset,55*tact_num_row,40,40))
                run = False

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
                    x_click, y_click = event.pos
                    A = math.pow((750 - x_click),2)
                    B = math.pow((50 - y_click),2)
                    dist = math.sqrt(A + B)
                    if dist < 25:
                        pygame.quit()


    def ColorMultiNode(self, tact_ID_list, side_list, on_time):
        
        if isinstance(tact_ID_list, int):
            if (tact_ID_list > 20) or side_list == "B":
                self.ColorNode(tact_ID_list,"B", on_time)
            else:
                self.ColorNode(tact_ID_list,"F", on_time)

        else:

            len_tact_list = len(tact_ID_list)
            len_side_list = len(side_list)
            if len_tact_list != len_side_list:
                print("ERROR:")
                print("ERROR:")
                print("ERROR: Tactor list given and vest side list given were not the same length.")
                print("ERROR: Each tactor must be given a vest side to vibrate on.")
                print("ERROR:")
                print("ERROR:")
                pygame.quit()

            # Converting seconds to milliseconds
            on_time = on_time*1000

            # time in millisecond from start program 
            start_time = pygame.time.get_ticks()
            current_time = pygame.time.get_ticks()

            # how long to show or hide
            delay = 50 # 50ms = 0.05s

            # time of next change 
            change_time = current_time + delay

            tactor_row_list = []
            tactor_col_list = []

            for tactor in range(len(tact_ID_list)):
                tactor = tactor

                # Front tact : [1:20], Back tact [21:40]
                # if tact # > 20, assumed to be reffering to tact on back 
                if tact_ID_list[tactor] > 20:
                    tact_ID_list[tactor] = tact_ID_list[tactor] - 20
                    side_list[tactor] = "B"
                elif tact_ID_list[tactor] > 40:
                    print("ERROR:")
                    print("ERROR:")
                    print("ERROR: Tact number mus be between 1 - 40.")
                    print("ERROR: Tact 01-20 refer to front or 'F' vest tacts.")
                    print("ERROR: Tact 21-40 refer to back  or 'B' vest tacts.")
                    print("ERROR:")
                    print("ERROR:")
                    pygame.quit()

                # Translating tact number to grid position
                tactor_row_list.append(math.ceil(tact_ID_list[tactor]/4))
                tactor_col_list.append(tact_ID_list[tactor]%4)

                if tactor_col_list[tactor] == 0:
                    tactor_col_list[tactor] = 4
            
            show = True
            run = True
            while run:
                current_time = pygame.time.get_ticks()
                elapsed_time = current_time - start_time

                # Checking if it is time to change
                if current_time >= change_time:
                    # time for next change 
                    change_time = current_time + delay
                    show = not show

                for tactor in range(len(tact_ID_list)):

                    # Default side is "F", "f"
                    side_offset = 0

                    if side_list[tactor] == "F":
                        side_offset = 0
                    elif side_list[tactor] == "B":
                        side_offset = 300

                    pygame.draw.rect(self.window, self._vars._black, (55*tactor_col_list[tactor]+side_offset,55*tactor_row_list[tactor],40,40))
                    
                    if show:
                        pygame.draw.rect(self.window, self._vars._red, (55*tactor_col_list[tactor]+side_offset,55*tactor_row_list[tactor],40,40))

                    pygame.display.update()

                    if elapsed_time > on_time:
                        pygame.draw.rect(self.window, self._vars._black, (55*tactor_col_list[tactor]+side_offset,55*tactor_row_list[tactor],40,40))
                        run = False

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
                            x_click, y_click = event.pos
                            A = math.pow((750 - x_click),2)
                            B = math.pow((50 - y_click),2)
                            dist = math.sqrt(A + B)
                            if dist < 25:
                                pygame.quit()

            
        

    def CycleNodes(self):
        for i in range(40):
            on_time = 0.125
            self.ColorNode(i+1,"F", on_time)


if __name__ == '__main__':

    # Demo for vest simulator
    sim_run = SimRun()
    
    # Function simply cycles through nodes
    sim_run.CycleNodes()
    
    vibrate_time = 0.125

    sim_run.ColorNode(0, "F", 1)

    # vibrating columns
    for ii in range(4):
        sim_run.ColorMultiNode([1+ii, 5+ii, 9+ii, 13+ii, 17+ii], ["F", "F", "F", "F", "F"], vibrate_time)
    for ii in range(4):
        sim_run.ColorMultiNode([1+ii, 5+ii, 9+ii, 13+ii, 17+ii], ["B", "B", "B", "B", "B"], vibrate_time)

    # vibrating rows
    for ii in range(5):
        sim_run.ColorMultiNode([1+4*ii, 2+4*ii, 3+4*ii, 4+4*ii, 21+4*ii, 22+4*ii, 23+4*ii, 24+4*ii], ["F", "F", "F", "F", "B", "B", "B", "B"], vibrate_time)

    # vibrating expanding/contracting ring front
    sim_run.ColorMultiNode([10,11], ["F","F"], vibrate_time)
    sim_run.ColorMultiNode([5,6,7,8,9,12,13,14,15,16], ["F","F", "F","F", "F","F", "F","F", "F","F" ], vibrate_time)
    sim_run.ColorMultiNode([1,2,3,4,17,18,19,20], ["F","F", "F","F", "F","F", "F","F"], vibrate_time)
    sim_run.ColorMultiNode([1,2,3,4,17,18,19,20], ["F","F", "F","F", "F","F", "F","F"], vibrate_time)
    sim_run.ColorMultiNode([5,6,7,8,9,12,13,14,15,16], ["F","F", "F","F", "F","F", "F","F", "F","F" ], vibrate_time)
    sim_run.ColorMultiNode([10,11], ["F","F"], vibrate_time)

    # vibrating expanding/contracting ring back
    sim_run.ColorMultiNode([10,11], ["B","B"], vibrate_time)
    sim_run.ColorMultiNode([5,6,7,8,9,12,13,14,15,16], ["B","B", "B","B", "B","B", "B","B", "B","B" ], vibrate_time)
    sim_run.ColorMultiNode([1,2,3,4,17,18,19,20], ["B","B", "B","B", "B","B", "B","B"], vibrate_time)
    sim_run.ColorMultiNode([1,2,3,4,17,18,19,20], ["B","B", "B","B", "B","B", "B","B"], vibrate_time)
    sim_run.ColorMultiNode([5,6,7,8,9,12,13,14,15,16], ["B","B", "B","B", "B","B", "B","B", "B","B" ], vibrate_time)
    sim_run.ColorMultiNode([10,11], ["B","B"], vibrate_time)

    # user controlled tactor vibration
    durationMillis = 100
    durationSecs = durationMillis/1000

    node = 0
    side = "front"

    print("Press Q to quit")

    done = False

    while not done:

        if msvcrt.kbhit():
            key = msvcrt.getwch()
            
            if key == "Q":
                break
            elif key == "w":
                node = node - 4
            elif key == "s":
                node = node + 4
            elif key == "a":
                node = node - 1
            elif key == "d":
                node = node + 1
            elif key == "f":
                side = "front"
            elif key == "b":
                side = "back"

            if node < 0:
                node = 0
            elif node > 40:
                node = 40
            
            if key == "Q":
                done = True
    
        print("node = ", node)

        if side == "front":
            sim_run.ColorNode(node, "F", durationSecs)
            time.sleep(durationSecs)
        else:
            sim_run.ColorNode(node, "B", durationSecs)
            time.sleep(durationSecs)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:  # or MOUSEBUTTONDOWN depending on what you want.
                x_click, y_click = event.pos
                A = math.pow((750 - x_click),2)
                B = math.pow((50 - y_click),2)
                dist = math.sqrt(A + B)
                if dist < 25:
                    pygame.quit()