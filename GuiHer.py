"""
LESSON: 3.4 - Program Structure
EXERCISE: Living Landscape
"""

#### ---- SET UP ---- ####

# ?
import pygame
import random
import time

pygame.init()

green = (50, 220, 50)
lgreen = (90, 255, 90)

blue = (50, 50, 220)
lblue = (90, 90, 255)

yellow = (220, 200, 10)
lyellow = (255, 240, 60)

red = (230, 20, 20)
lred = (255, 70, 70)

black = (0,0,0)
gray = (125, 125, 125)
white = (255, 255, 255)


width = 600
length = 600
# ?
window = pygame.display.set_mode([width, length])


#### ---- MAIN LOOP ---- ####

y = 0

difficulty = 1

placement = random.randint(0,3)

held_green = False
held_blue = False
held_yellow = False
held_red = False
total = 0
strike = 0
checkStrike = True
curscore = 0

# ?

run = True

clock = pygame.time.Clock()

clock.tick(120)


while run == True:
    
    def Overlay():
        gr_pad = pygame.Rect(25, 450, 100, 50)
        bl_pad = pygame.Rect(175, 450, 100, 50)
        ye_pad = pygame.Rect(325, 450, 100, 50)
        re_pad = pygame.Rect(475, 450, 100, 50)
        
        window.fill(black)
        
        pygame.draw.line(window, (white), (25, 475), (25, 0), 1)
        pygame.draw.line(window, (gray), (75, 475), (75, 0), 1)
        pygame.draw.line(window, (white), (125, 475), (125, 0), 1)
        
        pygame.draw.line(window, (white), (175, 475), (175, 0), 1)
        pygame.draw.line(window, (gray), (225, 475), (225, 0), 1)
        pygame.draw.line(window, (white), (275, 475), (275, 0), 1)
        
        pygame.draw.line(window, (white), (325, 475), (325, 0), 1)
        pygame.draw.line(window, (gray), (375, 475), (375, 0), 1)
        pygame.draw.line(window, (white), (425, 475), (425, 0), 1)
        
        pygame.draw.line(window, (white), (475, 475), (475, 0), 1)
        pygame.draw.line(window, (gray), (525, 475), (525, 0), 1)
        pygame.draw.line(window, (white), (575, 475), (575, 0), 1)
        
        pygame.draw.ellipse(window, (green), gr_pad)
        pygame.draw.ellipse(window, (blue), bl_pad)
        pygame.draw.ellipse(window, (yellow), ye_pad)
        pygame.draw.ellipse(window, (red), re_pad)
    
    
    def Random():
        
        global y
        global placement
        global held_green
        global held_blue
        global held_yellow
        global held_red
        global total
        global strike
        global checkStrike
        global curscore
        
        if y > 500:
            placement = random.randint(0,3)
            y = 0
        
        y += int(10 * difficulty)
        if y < 50:
            checkStrike = True
        if y > 450:
            if checkStrike == True:
                curscore = total
                checkStrike = False
            if y > 490:
                if total == curscore:
                    strike += 1
                
        
        gr_mpad = pygame.Rect(25, y, 100, 50)
        bl_mpad = pygame.Rect(175, y, 100, 50)
        ye_mpad = pygame.Rect(325, y, 100, 50)
        re_mpad = pygame.Rect(475, y, 100, 50)
    
        #pA = pygame.mixer.Sound("piano_A.mp3")
        #pC = pygame.mixer.Sound("piano_C.mp3")
        #pD = pygame.mixer.Sound("piano_D.mp3")
        #pF = pygame.mixer.Sound("piano_F.mp3")
        
        if placement == 0:
            if held_green == True:
                if y > 450:
                    pA.play()
                    total += 10
                    
            pygame.draw.ellipse(window, (green), gr_mpad)
        if placement == 1:
            if held_blue == True:
                if y > 450:
                    pC.play()
                    total += 10
                    
            pygame.draw.ellipse(window, (blue), bl_mpad)
        if placement == 2:
            if held_yellow == True:
                if y > 450:
                    pD.play()
                    total += 10
                    
            pygame.draw.ellipse(window, (yellow), ye_mpad)
        if placement == 3:
            if held_red == True:
                if y > 450:
                    pF.play()
                    total += 10
                    
            pygame.draw.ellipse(window, (red), re_mpad)
            
    
    def Lights():
        global y
        global placement
        global held_green
        global held_blue
        global held_yellow
        global held_red
        
        gr_pad = pygame.Rect(25, 450, 100, 50)
        bl_pad = pygame.Rect(175, 450, 100, 50)
        ye_pad = pygame.Rect(325, 450, 100, 50)
        re_pad = pygame.Rect(475, 450, 100, 50)
            
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                held_green = True
            if event.type == pygame.KEYUP and event.key == pygame.K_a:
                held_green = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                held_blue = True
            if event.type == pygame.KEYUP and event.key == pygame.K_s:
                held_blue = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                held_yellow = True
            if event.type == pygame.KEYUP and event.key == pygame.K_d:
                held_yellow = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                held_red = True
            if event.type == pygame.KEYUP and event.key == pygame.K_f:
                held_red = False
            
        if held_green == True:
            pygame.draw.ellipse(window, (lgreen), gr_pad)
        if held_blue == True:
            pygame.draw.ellipse(window, (lblue), bl_pad)
        if held_yellow == True:
            pygame.draw.ellipse(window, (lyellow), ye_pad)
        if held_red == True:
            pygame.draw.ellipse(window, (lred), re_pad)
        
    def Score():
        events = pygame.event.get()
        global total
        
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if held_green == True:
                    if placement == 0:
                        y = 0
                        total +=10
                    else:
                        total -= 10
                if held_blue == True:
                    if placement == 1:
                        y = 0
                        total +=10
                    else:
                        total -= 10
                if held_yellow == True:
                    if placement == 2:
                        y = 0
                        total +=10
                    else:
                        total -= 10
                if held_red == True:
                    if placement == 3:
                        y = 0
                        total +=10
                    else:
                        total -= 10
                    
        
    Overlay()
    
    Random()
    
    Lights()
        
    print(total)
    
    print(strike)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    x = 0


# Turn in your Coding Exercise.

    
