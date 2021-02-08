#-*- coding: utf-8 -*-
import pygame
import UI
import Setting_Value
import time
import node
import map
import effect
import threading
import MapList

pygame.display.init()
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

size = Setting_Value.Display_Set.display_size
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

# state
INTRO_STATE = True
MAIN_STATE = False
GAME_STATE = False
MAIN_FADE_OUT_STATE = False
EFFECT_ON = False
GAME_READY_STATE = False
PAUSE = False
COMPLETE_STATE = False

tmp = pygame.Surface(Setting_Value.Display_Set.display_size)
tmp.fill(UI.BLACK)

start_button = UI.button_main(screen, "START", Setting_Value.Display_Set.main_btn_start_x, Setting_Value.Display_Set.main_btn_start_y, 60, True)
option_button = UI.button_main(screen, "OPTION", Setting_Value.Display_Set.main_btn_option_x, Setting_Value.Display_Set.main_btn_option_y, 60, False)
exit_button = UI.button_main(screen, "EXIT", Setting_Value.Display_Set.main_btn_exit_x, Setting_Value.Display_Set.main_btn_exit_y, 60, False)
Easy_Hard = UI.button_SongList(screen, "EASY", Setting_Value.Display_Set.easy_x, Setting_Value.Display_Set.easy_y, "HARD", Setting_Value.Display_Set.hard_x, Setting_Value.Display_Set.hard_y)

# Font and Image
main_font = pygame.font.Font("Resource\Font\digital.ttf", 120)

info_font1 = pygame.font.Font("Resource\Font\InterparkGothicOTFM.otf", 40)
info_font2 = pygame.font.Font("Resource\Font\InterparkGothicOTFM.otf", 80)

loading_font = pygame.font.Font("Resource\Font\digital.ttf", 200)
rank_font = pygame.font.Font("Resource\Font\CookieRun.ttf", 300)
number_font = pygame.font.Font("Resource\Font\digital.ttf", 120)
score_font = pygame.font.Font("Resource\Font\digital.ttf", 100)
combo_font = pygame.font.Font("Resource\Font\digital.ttf", 80)
judge_font = pygame.font.Font("Resource\Font\digital.ttf", 80)

main_bck = pygame.image.load("Resource\main_background.jpg").convert()

background = pygame.image.load("Resource\_bg.jpg").convert()
frame = pygame.image.load("Resource\_frame\_frame.png").convert_alpha()
result_frame = pygame.image.load("Resource\_frame\_result.png").convert_alpha()
 
# Back Button
Back_Btn = UI.button_back(screen, 20, 10)

# Song List
List = UI.SongList(screen)
i = 0
for Map in MapList.MapList:
    List.append(Map.get_title(), pygame.image.load("Resource\image" + str(i) + ".jpg").convert(), Map.get_artist(), Map.get_level())
    i += 1

# Background Music

Selected = 1
alpha = 0
comp = 0

# About Game

node1 = node.node(Setting_Value.Display_Set.node1_x, Setting_Value.Display_Set.node_y, 100, 100, 1, screen)
node2 = node.node(Setting_Value.Display_Set.node2_x, Setting_Value.Display_Set.node_y, 100, 100, 2, screen)
node3 = node.node(Setting_Value.Display_Set.node3_x, Setting_Value.Display_Set.node_y, 100, 100, 3, screen)
node4 = node.node(Setting_Value.Display_Set.node4_x, Setting_Value.Display_Set.node_y, 100, 100, 4, screen)

node_group = pygame.sprite.RenderPlain([node1, node2, node3, node4])

time_bar = UI.TimeBar(screen)

NoteList = []
NoteList_Drawer = []

Note_Count = 0
MODE_NOTE_FALL = False

stack = -25

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def print_effect(select):
    if select == 1:
        effect.note_anim1.play()
    elif select == 2:
        effect.note_anim2.play()
    elif select == 3:
        effect.note_anim3.play()
    elif select == 4:
        effect.note_anim4.play()

def print_node():
    if MODE_NOTE_FALL:
        for i in range(map.killed_note(0), Note_Count):
            NoteList_Drawer[i].draw(screen)
            NoteList_Drawer[i].update(0)
            
# main loop
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            pygame.mixer.music.stop()
            done = True
        
        if event.type == pygame.KEYDOWN and (INTRO_STATE == True): # key board down event, in INTRO STATE
            if event.key == pygame.K_UP: # up key
                if not start_button.get_selected() and not option_button.get_selected() and exit_button.get_selected():
                    start_button.update(0)
                    option_button.update(1)
                    exit_button.update(0)
                elif not start_button.get_selected() and option_button.get_selected() and not exit_button.get_selected():
                    start_button.update(1)
                    option_button.update(0)
                    exit_button.update(0)
                break
                    
            if event.key == pygame.K_DOWN: # down key
                if start_button.get_selected() and not option_button.get_selected() and not exit_button.get_selected():
                    start_button.update(0)
                    option_button.update(1)
                    exit_button.update(0)
                elif not start_button.get_selected() and option_button.get_selected() and not exit_button.get_selected():
                    start_button.update(0)
                    option_button.update(0)
                    exit_button.update(1)
                break
            
            if event.key == pygame.K_KP_ENTER: # kp enter key
                pygame.mixer.Sound("Sound\sound2.ogg").play()
                if start_button.get_selected() and not option_button.get_selected() and not exit_button.get_selected():
                    INTRO_STATE = False
                    MAIN_STATE = True
                elif not start_button.get_selected() and option_button.get_selected() and not exit_button.get_selected():
                    INTRO_STATE = True
                elif not start_button.get_selected() and not option_button.get_selected() and exit_button.get_selected():
                    pygame.mixer.music.fadeout(2700)
                    pygame.time.delay(3000)
                    pygame.mixer.music.pause()
                    pygame.mixer.music.stop()
                    pygame.time.delay(500)
                    exit()
                break
            
        if event.type == pygame.KEYDOWN and (MAIN_STATE == True) and (MAIN_FADE_OUT_STATE == False): # key board down event, in MAIN STATE
            if event.key == pygame.K_UP:
                List.update(True,False)
            if event.key == pygame.K_DOWN:
                List.update(False,True)
            if event.key == pygame.K_KP_ENTER: # go to GAME READY STATE
                List.update(False, False, False, False, True)
                
                GAME_READY_STATE = True
                pygame.mixer.music.fadeout(1500)
                List.isGameReadyMode(True)
                start_time = time.time()
            if event.key == pygame.K_ESCAPE: # back to INTRO STATE
                MAIN_STATE = False
                INTRO_STATE = True
                pygame.mixer.music.stop()
                pygame.time.delay(300)
            break
        
        if (GAME_STATE == True) and pygame.mixer.get_busy() and (PAUSE == False):
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                GAME_STATE = False
                
            if event.type == pygame.KEYDOWN: # key board down event
                if event.key == pygame.K_d: # node key
                    thread_effect = threading.Thread(target=print_effect(1))
                    thread_effect.start()
                    for i in range(map.killed_note(0), Note_Count):
                        NoteList_Drawer[i].update(1, True)
                    node1.update(True, False, 1)
                if event.key == pygame.K_f:
                    thread_effect = threading.Thread(target=print_effect(2))
                    thread_effect.start()
                    for i in range(map.killed_note(0), Note_Count):
                        NoteList_Drawer[i].update(2, True)
                    node2.update(True, False, 2)
                if event.key == pygame.K_k:
                    thread_effect = threading.Thread(target=print_effect(3))
                    thread_effect.start()
                    for i in range(map.killed_note(0), Note_Count):
                        NoteList_Drawer[i].update(3, True)
                    node3.update(True, False, 3)
                if event.key == pygame.K_l:
                    thread_effect = threading.Thread(target=print_effect(4))
                    thread_effect.start()
                    for i in range(map.killed_note(0), Note_Count):
                        NoteList_Drawer[i].update(4, True)
                    node4.update(True, False, 4)
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.pause()
                    PAUSE = True
                break

            if event.type == pygame.KEYUP: # key board up event
                if event.key == pygame.K_d:
                    effect.note_anim1.stop()
                if event.key == pygame.K_f:
                    effect.note_anim2.stop()
                if event.key == pygame.K_k:
                    effect.note_anim3.stop()
                if event.key == pygame.K_l:
                    effect.note_anim4.stop()
                break

    if GAME_STATE:
        while COMPLETE_STATE: # complete state
            # background
            screen.blit(background, [0,0])
            screen.blit(frame, [0,0])

            node_group.draw(screen)
            tmp.set_alpha(150)
            screen.blit(tmp, [0,0])
            
            screen.blit(result_frame, [0,0])
            
            score_txt, rank_txt, rank_color, count = map.result()

            screen.blit(info_font2.render("YOU SCORED", True, UI.WHITE), (400, 247)) # print score
            screen.blit(info_font1.render("out of a possible 100000 points", True, UI.WHITE), (400, 337))
            
            screen.blit(info_font1.render("PERFECT", True, UI.WHITE), (400, 577))
            screen.blit(info_font1.render("GREAT", True, UI.WHITE), (400, 627))
            screen.blit(info_font1.render("GOOD", True, UI.WHITE), (400, 677))
            screen.blit(info_font1.render("BAD", True, UI.WHITE), (400, 727))
            screen.blit(info_font1.render("MISS", True, UI.WHITE), (400, 777))
            
            screen.blit(info_font2.render(str(score_txt), True, UI.COMBO), (945, 247))
            
            screen.blit(info_font1.render(str(count[0]), True, UI.COMBO), (650, 577))
            screen.blit(info_font1.render(str(count[1]), True, UI.COMBO), (650, 627))
            screen.blit(info_font1.render(str(count[2]), True, UI.COMBO), (650, 677))
            screen.blit(info_font1.render(str(count[3]), True, UI.COMBO), (650, 727))
            screen.blit(info_font1.render(str(count[4]), True, UI.COMBO), (650, 777))
            
            rank_th = rank_font.render("「" + rank_txt + "」", True, rank_color)
            rank_th.set_alpha(50)
            screen.blit(rank_th, (1115, 303))
            rank = rank_font.render(rank_txt, True, rank_color)
            screen.blit(rank, (1250, 303))
            
            if Back_Btn.update(): # go to MAIN STATE, mouse click
                pygame.time.delay(200)
                COMPLETE_STATE = False
                GAME_STATE = False
                GAME_READY_STATE = False
                MAIN_STATE = True
                List.isGameReadyMode(False)
                map.initialize()
                time_bar.initialize()
                for i in range(0, MapList.MapList[List.get_selected_Song()].get_note_count()):
                    NoteList.pop()
                    NoteList_Drawer.pop()
                break

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # go to MAIN STATE, keyboard esc
                        pygame.time.delay(200)
                        COMPLETE_STATE = False
                        GAME_STATE = False
                        GAME_READY_STATE = False
                        MAIN_STATE = True
                        List.isGameReadyMode(False)
                        map.initialize()
                        time_bar.initialize()
                        for i in range(0, MapList.MapList[List.get_selected_Song()].get_note_count()):
                            NoteList.pop()
                            NoteList_Drawer.pop()
                        break

            pygame.display.flip()
            clock.tick(120)

        tmp.set_alpha(75)
        screen.blit(tmp, [0, 0])

        while PAUSE: # pause state
            if Back_Btn.update(): # go to MAIN STATE, mouse click
                pygame.mixer.unpause()
                MapList.MapList[List.get_selected_Song()].sound.stop()
                GAME_STATE = False
                GAME_READY_STATE = False
                MAIN_STATE = True
                List.isGameReadyMode(False)
                # Clear the NoteList When Game Finished
                for i in range(0, MapList.MapList[List.get_selected_Song()].get_note_count()):
                    NoteList.pop()
                    NoteList_Drawer.pop()
                break

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # back to GAME STATE, keyboard esc
                        pygame.time.delay(200)
                        pygame.mixer.unpause()
                        PAUSE = False
                        GAME_READY_STATE = False

            pygame.display.flip()
            clock.tick(120)

        while GAME_READY_STATE: # game ready state
            end_time = MapList.MapList[List.get_selected_Song()].playtime

            # background
            screen.blit(background, [0,0])
            screen.blit(frame, [0,0])

            node_group.draw(screen)
            tmp.set_alpha(alpha)
            screen.blit(tmp, [0,0])
            gap = time.time() - start_time # get time
            if gap < 1: # count down per second
                title = loading_font.render("3", True, UI.GRAY)
            elif 1 <= gap < 2:
                title = loading_font.render("2", True, UI.GRAY)
            elif 2 <= gap < 3:
                title = loading_font.render("1", True, UI.GRAY)
            else:
                # Get Selected Mode of Song(Easy or Hard)
                MapList.MapList[List.get_selected_Song()].set_mode(Easy_Hard.get_mode()) # only easy mode is available
                # print(Easy_Hard.get_mode())
                # Right before Game Begin
                for i in range(0, MapList.MapList[List.get_selected_Song()].get_note_count()):
                    # note initializeing
                    # case Normal Note
                    NoteList.append(map.note(screen, 100, 25, MapList.MapList[List.get_selected_Song()].get_note(), MapList.MapList[List.get_selected_Song()].speed))
                    MapList.MapList[List.get_selected_Song()].move_index()
                    NoteList_Drawer.append(pygame.sprite.RenderPlain(NoteList[i]))

                for i in range(0, MapList.MapList[List.get_selected_Song()].get_note_count()):
                    # 노트 재 할당(노트 위치 초기화)
                    NoteList[i].re_init()

                MapList.MapList[List.get_selected_Song()].sound.play()
                Note_Count = 0
                # revising value of the sync_time  = comp
                comp = Setting_Value.Display_Set.note_init_pos / (MapList.MapList[List.get_selected_Song()].speed * 60)
                start_time = time.time()
                break
            screen.blit(title, Setting_Value.Display_Set.loading)

            pygame.display.flip()
            clock.tick(120)

        # When Game is Playing
        while pygame.mixer.get_busy() and not PAUSE:
            end_time = MapList.MapList[List.get_selected_Song()].playtime # get last note time
            if time.time() - start_time + 0.2 > end_time: # check, game is done
                print("complete")
                pygame.mixer.quit()
                COMPLETE_STATE = True
                break
            
            if time.time() - start_time >= MapList.MapList[List.get_selected_Song()].get_sync() - comp: # note print
                if MapList.MapList[List.get_selected_Song()].move_sync_index():
                    MODE_NOTE_FALL = True
                    Note_Count += 1
                    MapList.MapList[List.get_selected_Song()].move_index()
            
            screen.fill(UI.BLACK)
            # background game is playing
            screen.blit(background, [0,0])
            screen.blit(frame, [0,0])
            
            # screen.blit(tmp, [0,0])
            time_bar.update()
            node_group.draw(screen)
            # score block
            score_text = main_font.render(str(map.combo(0)), True, UI.COMBO)
            score_text.set_alpha(UI.ALPHA)
            text_rect = score_text.get_rect()
            text_rect.right = 1074 # align to right to 150px
            text_rect.top = 380
            combo_text = combo_font.render("COMBO", True, UI.COMBO)
            combo_text.set_alpha(UI.ALPHA)
            number_text = score_font.render(str(map.score(0)), True, UI.COMBO)
            number_rect = number_text.get_rect()
            number_rect.right = 1900
            number_rect.top = 15
            
            # judge
            a, b, c = map.judge()
            judge_text = judge_font.render(a, True, b) # color should be chaanged
            judge_text.set_alpha(UI.BLPHA)
            
            #thread_effect = threading.Thread(target=print_effect)
            #thread_effect.start()
            
            if(UI.ALPHA != 255):
                UI.ALPHA += 51
                
            if(UI.BLPHA != 0 and stack <= 5): # fade out, ease-out
                stack += 1
                UI.BLPHA += 2 * stack - 10
            else:
                stack = -25
                    
            screen.blit(main_font.render("8888", True, UI.GRAY), Setting_Value.Display_Set.combo_th)
            screen.blit(combo_text, Setting_Value.Display_Set.combo_txt)
            screen.blit(score_text, text_rect)
            screen.blit(judge_text, c)
            screen.blit(number_text, number_rect)
            
            thread_note = threading.Thread(target=print_node)
            thread_note.start()
            
            node_group.update(False, False)
            
            effect.note_anim1.blit(screen, (Setting_Value.Display_Set.node1_x - 50, Setting_Value.Display_Set.node_y - 932))
            effect.note_anim2.blit(screen, (Setting_Value.Display_Set.node2_x - 50, Setting_Value.Display_Set.node_y - 932))
            effect.note_anim3.blit(screen, (Setting_Value.Display_Set.node3_x - 50, Setting_Value.Display_Set.node_y - 932))
            effect.note_anim4.blit(screen, (Setting_Value.Display_Set.node4_x - 50, Setting_Value.Display_Set.node_y - 932))
    
            effect.bomb_anim1.blit(screen, (Setting_Value.Display_Set.node1_x - 148, Setting_Value.Display_Set.node_y - 230))
            effect.bomb_anim2.blit(screen, (Setting_Value.Display_Set.node2_x - 148, Setting_Value.Display_Set.node_y - 230))
            effect.bomb_anim3.blit(screen, (Setting_Value.Display_Set.node3_x - 148, Setting_Value.Display_Set.node_y - 230))
            effect.bomb_anim4.blit(screen, (Setting_Value.Display_Set.node4_x - 148, Setting_Value.Display_Set.node_y - 230))
    
            effect.glow_anim.blit(screen, (550, 0))
                        
            pygame.display.flip()
            clock.tick(120)

    # --- INTRO SCENE LOOP ---
    elif INTRO_STATE:
        # Intro Scene
        screen.fill(UI.BLACK)
        screen.blit(main_bck, [0,0])

        start_button.draw()
        option_button.draw()
        exit_button.draw()
            
        pygame.display.flip()
        clock.tick(120)

    elif MAIN_STATE: # main state
        # Songs List
        screen.fill(UI.BLACK)
        
        now_item = List.get_selected_Song()

        List.update()
        
        if Back_Btn.update() and MAIN_FADE_OUT_STATE == False:
            MAIN_STATE = False
            INTRO_STATE = True
            pygame.time.delay(100)
        if Back_Btn.update() and MAIN_FADE_OUT_STATE:
            MAIN_FADE_OUT_STATE = False
            pygame.time.delay(100)

        if GAME_READY_STATE: # fade out screen
            gap = (time.time() - start_time)
            if gap < 2.5:
                tmp.set_alpha(gap * 155)
                screen.blit(tmp, [0, 0])
            elif 2 <= gap < 4.8 :
                alpha = 255 - (gap - 2) * 45
                tmp.set_alpha(alpha)
                end_time = MapList.MapList[List.get_selected_Song()].playtime

                # background
                screen.blit(background, [0,0])
                screen.blit(frame, [0,0])

                time_bar.set_endTime(end_time)
                
                node_group.draw(screen)
                screen.blit(tmp, [0, 0])
                if gap >= 4.6 :
                    GAME_STATE = True
                    MAIN_STATE = False
                    PAUSE = False
                    MapList.MapList[List.get_selected_Song()].init_index()
                    MapList.MapList[List.get_selected_Song()].set_speed(List.SongSpeed-1)
                    map.killed_note(0, True)
                    map.combo(0, True)
                    map.score(-1, MapList.MapList[List.get_selected_Song()])
                    start_time = time.time()

        pygame.display.flip()
        clock.tick(120)