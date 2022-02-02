import pygame, sys, os, time 
from random import *
import os

level = 1
gameover_flag = False
#game_start
pygame.init()
screen_size = (800,600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
#background
GUI_DIR = os.path.join(os.path.dirname(__file__), 'GUI')
bg_surface = pygame.image.load(os.path.join(GUI_DIR, 'background.jpg')).convert_alpha()
bg_surface = pygame.transform.scale(bg_surface, screen_size)
#text
font = pygame.font.Font(os.path.join(GUI_DIR, 'FONT', 'Roboto-LightItalic.ttf'), 30)
#bubble
bubble_surface = pygame.image.load(os.path.join(GUI_DIR, 'bubble.png')).convert_alpha()
bubble_surface = pygame.transform.scale(bubble_surface, (100, 100))
#game pic
brain = pygame.image.load(os.path.join(GUI_DIR, 'brain.png')).convert_alpha()
brain = pygame.transform.scale(brain, (405, 335))
#gameover
gameover_surface = pygame.image.load(os.path.join(GUI_DIR, 'gameover.png')).convert_alpha()
#buttons
play_button = pygame.image.load(os.path.join(GUI_DIR, 'play_button.png')).convert_alpha()
play_button = pygame.transform.scale(play_button, (215, 50))
play_rect = play_button.get_rect(center = (200 , 500))

rules_button = pygame.image.load(os.path.join(GUI_DIR, 'rules_button.png')).convert_alpha()
rules_button = pygame.transform.scale(rules_button, (215, 50))
rules_rect = rules_button.get_rect(center = (200 + 215, 500))

exit_button = pygame.image.load(os.path.join(GUI_DIR, 'exit_button.png')).convert_alpha()
exit_button = pygame.transform.scale(exit_button, (215, 50))
exit_rect = exit_button.get_rect(center = (200 + 215 + 215 + 2, 500))

home_button = pygame.image.load(os.path.join(GUI_DIR, 'home.png')).convert_alpha()
home_button = pygame.transform.scale(home_button, (30  , 30))
home_rect = home_button.get_rect(topleft = (10,10))

next_level_surface = pygame.image.load(os.path.join(GUI_DIR, "next_level.png"))
next_level_surface = pygame.transform.scale(next_level_surface, (215, 50))
next_level_rect = next_level_surface.get_rect(center = (415, 500))

#STUDENT_ID
STUDENT_ID_surface = font.render('''MOHAMMAD SHABIB  19290116''', True, (255,0,0))
#levelup
level_up_surface = pygame.image.load(os.path.join(GUI_DIR, 'level_up.png')).convert_alpha()
level_up_surface = pygame.transform.scale(level_up_surface, (325, 425))
#sound
level_up_sound = pygame.mixer.Sound(os.path.join(GUI_DIR, 'SOUND', 'cheers.wav'))
lose_sound = pygame.mixer.Sound(os.path.join(GUI_DIR, 'SOUND', 'lose.wav'))

current_time = 0
def disp_bubbles(nums_size): #display the nums and return a list of the displayed nums
    screen.fill((0, 0, 0))
    
    pause_time = pygame.time.get_ticks() #get current time 
    bubble_pos =  randrange(1,screen_size[0] - 100, 100),randrange(1,screen_size[1] - 100, 100) #rand pos 
    i = 0
    nums = []
    nums.append(randrange(100, 10000))
    while i < nums_size:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None

        screen.blit(bg_surface, (0,0))
        level_surface = font.render(f"Level: {level}", True, (255,0,0))    #updating the level
        screen.blit(level_surface, (0,0))    #showing the lvl    

        screen.blit(bubble_surface, bubble_pos) #show the bubble
        num_surface = font.render(f"{nums[i]}", True, (255,0,0))
        num_rect = num_surface.get_rect(center = (bubble_pos[0] + 50, bubble_pos[1] + 50)) #print the num inside the bubble
        screen.blit(num_surface, num_rect)
        
        current_time = pygame.time.get_ticks() #get current time
        if current_time - pause_time > randint(1000, 2000): #this keeps the bubble on display for 1-2secs, after 1.5sec change the pos and the num and rest pause time
            print(nums[i])
            nums.append(randrange(100, 10000))
            bubble_pos =  randrange(1,screen_size[0] - 100, 100),randrange(1,screen_size[1] - 100, 100) 
            pause_time = pygame.time.get_ticks()
            i += 1


          
        pygame.display.update()
        clock.tick(60)
    print("xxxxxxx")
    return nums

def check_bubbles(nums): #check the nums if correct
    screen.fill((0, 0, 0))
    user_num = ''
    i = 0
    flag = True
    while i < len(nums) - 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
                if flag:
                    if event.key == pygame.K_BACKSPACE: #delete the last digit
                        user_num = user_num[:-1]
                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN: #stop taking any more inputs and set flag to False
                        flag = False
                    if event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 \
                    or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 \
                    or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 \
                    or event.key == pygame.K_9: #this makes the input only numbers
                        user_num += event.unicode

        screen.blit(bg_surface, (0,0))
        level_surface = font.render(f"Level: {level}", True, (255,0,0))
        screen.blit(level_surface, (0,0))
        #asking for input
        text_surface = font.render(f"Enter the {i + 1}'th number", True, (255,0,0))
        screen.blit(text_surface, (screen_size[0]/2 - 140, screen_size[1]/2- 50 ))
        screen.blit(bubble_surface, (screen_size[0]/2 - 70, screen_size[1]/2))
        input_surface = font.render(user_num, True, (255,0,0))
        screen.blit(input_surface, (screen_size[0]/2 - 60, screen_size[1]/2 + 37))
        ####
        if not flag: #to check the input after its finished
            if int(user_num) != nums[i]: 
                return False
            else: 
                flag = True
                user_num = ''
                i += 1
            
        pygame.display.update()
        clock.tick(60)
    return True

def Level_up_screen():
    level_up_sound.play()
    screen.fill((0, 0, 0))
    pause_time = pygame.time.get_ticks()
    while True:
        click = False   
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if next_level_rect.collidepoint(mouse_pos) and click:
                level_up_sound.stop()
                return         
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        current_time = pygame.time.get_ticks()

        screen.blit(bg_surface, (0,0)) 
        level_surface = font.render(f"Level: {level}", True, (255,0,0))
        screen.blit(level_surface, (0,0))
        screen.blit(level_up_surface, (250,80))
        screen.blit(next_level_surface, next_level_rect)

        if current_time - pause_time > 2000:
            level_up_sound.stop()


        pygame.display.update()
        clock.tick(60)

def game(): #starting the game
    global level
    global gameover_flag
    level = 1
    screen.fill((0, 0, 0)) #resting the display
    nums_size = 5
    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get(): #check for events key or mouse
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameover_flag = False
                    return

        screen.blit(bg_surface, (0,0)) 
        nums = disp_bubbles(nums_size) 
        if nums is None:#if num is none return to the main menu
            gameover_flag = False
            return 
        check = check_bubbles(nums)
        if check is None: #if check is none return to the main menu
            gameover_flag = False
            return 
        if check == False: #if check is false that means lose
            return "gameover"
        if check == True: #if true mean level up
            nums_size += 1
            level += 1
            Level_up_screen()
        pygame.display.update()
        clock.tick(60)

def rules():
    screen.fill((0, 0, 0))
    text_font = pygame.font.Font(os.path.join(GUI_DIR, 'FONT', 'Roboto-LightItalic.ttf'), 20)
    while True:
        click = False   
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if home_rect.collidepoint(mouse_pos) and click:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
        screen.blit(bg_surface, (0,0))
        screen.blit(home_button,home_rect)  

        rules = text_font.render("*When the game starts the initial size of the pattern is : 5. It will increase by 1 each level.", True, (255, 0, 0))
        screen.blit(rules, (40, 100))
        rules = text_font.render("*In order to move to the next level you need to memorize all the numbers in order.", True, (255, 0, 0))
        screen.blit(rules, (40, 150))
        rules = text_font.render("*E.X: if the pattern was 32 99, you can't enter 99 33, the pattern should be in order.", True, (255, 0, 0))
        screen.blit(rules, (40, 200))
        rules = text_font.render("*After entering each number you must press the 'ENTER' key", True, (255, 0, 0))
        screen.blit(rules, (40, 250))
        rules = text_font.render("*If you want to go back to home menu press 'ESC' at anytime.", True, (255, 0, 0))
        screen.blit(rules, (40, 300))

        pygame.display.update()
        clock.tick(60)

def main_menu(): #home page
    global gameover_flag 
    gameover_flag = False
    while True:
        click = False        
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        if play_rect.collidepoint(mouse_pos) and click: #if play button clicked
            lose_sound.stop()
            if game() == "gameover": #run the game and check if the result is losing to change the gameover flag
                lose_sound.play()
                gameover_flag = True
        if rules_rect.collidepoint(mouse_pos) and click: #rules page
            lose_sound.stop()
            rules()
        if exit_rect.collidepoint(mouse_pos) and click: #exit
            pygame.quit()
            sys.exit()


        screen.blit(bg_surface, (0,0)) #display background
        screen.blit(play_button, play_rect)
        screen.blit(rules_button, rules_rect)
        screen.blit(exit_button, exit_rect)
        if gameover_flag:            
            screen.blit(gameover_surface, (125,70))
        else:
            screen.blit(brain, (190, 70))

        screen.blit(STUDENT_ID_surface, (0, 0))
        

        pygame.display.update() #update the display every rotation
        clock.tick(60) # max fram per sec

#window title and icon
pygame.display.set_caption("Memory Game")
icon = pygame.image.load(os.path.join(GUI_DIR, "brain.png"))
pygame.display.set_icon(icon)
#starting the software
main_menu()
