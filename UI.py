#-*- coding: utf-8 -*-
import pygame
import time
import threading
import MapList
import Setting_Value
import map

pygame.init()

# Defined Color
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (32,32,64)
COMBO = (128,128,192)
LIGHT_GRAY = (64, 64, 64)
NOT_SELECTED = (129,129,155)
SETTING_BAR = (62, 96, 111)
EASY = (12, 232, 118)
HARD = (232, 44, 12)
TIMEBAR = (32,32,64)
ALPHA = 255
BLPHA = 0

MODE_GAME_READY = False
            
class button_main(pygame.sprite.Sprite): # intro state button
    def __init__(self, screen, msg, x, y, font_size, selected, action=None):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.msg = msg
        self.font_size = font_size
        self.action = action
        self.screen = screen
        self.selected = selected

    def update(self, selected):
        if selected == 0:
            font = pygame.font.Font('Resource\Font\InterparkGothicOTFB.otf', self.font_size)
            txt = font.render(self.msg, True, NOT_SELECTED)
            self.selected = False
        elif selected == 1:
            font = pygame.font.Font('Resource\Font\InterparkGothicOTFB.otf', self.font_size)
            txt = font.render(self.msg, True, WHITE)
            self.selected = True
            pygame.mixer.Sound("Sound\sound1.ogg").play()

        self.screen.blit(txt, [self.x, self.y])
    
    def get_selected(self):
        return self.selected
    
    def draw(self):
        if self.selected == False:
            font = pygame.font.Font('Resource\Font\InterparkGothicOTFB.otf', self.font_size)
            txt = font.render(self.msg, True, NOT_SELECTED)
        elif self.selected == True:
            font = pygame.font.Font('Resource\Font\InterparkGothicOTFB.otf', self.font_size)
            txt = font.render(self.msg, True, WHITE)

        self.screen.blit(txt, [self.x, self.y])

class button_SongList(pygame.sprite.Sprite): # easy, hard button
    selected = 1
    # Easy = 1 / Hard = 2
    def __init__(self, screen, button1_msg,  button1_x, button1_y, button2_msg,  button2_x, button2_y, action = None):
        pygame.sprite.Sprite.__init__(self)
        self.button1_x = button1_x
        self.button1_y = button1_y
        self.button1_msg = button1_msg
        self.button2_x = button2_x
        self.button2_y = button2_y
        self.button2_msg = button2_msg
        self.screen = screen

    def update(self, selected):
        if selected ==1:
            font = pygame.font.Font('Resource\Font\InterparkGothicOTFM.otf', 60)
            self.easy = font.render(self.button1_msg, True, EASY)
            font = pygame.font.Font('Resource\Font\InterparkGothicOTFM.otf', 60)
            self.hard = font.render(self.button2_msg, True, NOT_SELECTED)
            self.selected = 1
        if selected == 2:
            font = pygame.font.Font('Resource\Font\InterparkGothicOTFM.otf', 60)
            self.hard = font.render(self.button2_msg, True, HARD)
            font = pygame.font.Font('Resource\Font\InterparkGothicOTFM.otf', 60)
            self.easy = font.render(self.button1_msg, True, NOT_SELECTED)
            self.selected = 2

        #self.screen.blit(self.easy, [self.button1_x, self.button1_y])
        #self.screen.blit(self.hard, [self.button2_x, self.button2_y])

    def get_mode(self):
        return self.selected

class button_back(pygame.sprite.Sprite): # back button
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen = screen
        
    def update(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

        back_button = pygame.image.load("Resource\_Icon\_back.png").convert_alpha()
        back_button.set_alpha(50)
        self.screen.blit(back_button, [self.x, self.y])
        
        if self.x + 100 > self.mouse[0] > self.x and self.y < self.mouse[1] < self.y + 100: # mouse click event range
            if self.click[0] == 1:
                return True

class SongList(pygame.sprite.Sprite): # song list button
    List= []
    List_map = []
    List_font = []
    List_Background = []
    List_SongInfo = []
    list_focus = 0
    list_count = 0

    start = Setting_Value.Display_Set.title[1] - 50
    margin = 50
    margin_background = 600

    MODE_FADE_OUT = False
    MODE_SCROLL_DOWN = False
    MODE_SCROLL_UP = False
    speed = 0

    first_pos = 0
    pos = 0

    alpha_value = 180
    alpha_value_change_speed = 0

    SongSpeed = 3

    main_font = pygame.font.Font('Resource\Font\InterparkGothicOTFM.otf', 35)
    font = pygame.font.Font('Resource\Font\InterparkGothicOTFM.otf', 60)
    font2 = pygame.font.Font('Resource\Font\InterparkGothicOTFM.otf', 55)
    font3 = pygame.font.Font('Resource\Font\InterparkGothicOTFM.otf', 40)
    font4 = pygame.font.Font('Resource\Font\SansJP.otf', 40)
    
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([500, 1600])
        self.background = pygame.Surface(Setting_Value.Display_Set.display_size)
        self.screen = screen

    def append(self,title, bg_image, artist,difficulty):
        self.List.append(title)
        self.List_font.append(self.font.render(title, True, NOT_SELECTED))
        self.List_Background.append(bg_image)
        self.List_map.append(map)
        self.List_SongInfo.append(SongInfo(self.screen, title, artist, None, 0, difficulty, None))
        self.list_count +=1

    def update(self, up= False, down= False, Sort_A = False, Sort_B = False, enter= False, SpeedUp = False, SpeedDown = False):
        global list_focus
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        # gap size between two items
        self.margin = 50
        self.screen.blit(self.background, [0, self.pos])
        
        selected = pygame.Surface([1600,70])
        selected.fill(NOT_SELECTED)
        
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)

        if up and self.list_focus > 0:
            if self.MODE_SCROLL_UP:
                return False
            self.list_focus -= 1
            #print(self.list_focus)
            self.start += 240
            sound = pygame.mixer.Sound("Sound\sound1.ogg")
            sound.play()
            self.MODE_SCROLL_UP = True

        if down and self.list_focus < self.list_count-1 :
            if self.MODE_SCROLL_DOWN:
                return False
            self.list_focus += 1
            #print(self.list_focus)
            self.start -= 240
            sound = pygame.mixer.Sound("Sound\sound1.ogg")
            sound.play()
            self.MODE_SCROLL_DOWN = True

        if enter:
            self.MODE_FADE_OUT = True
            self.cover = pygame.Surface(Setting_Value.Display_Set.display_size)
            self.start_time = time.time()
            self.cover.fill(BLACK)
            pygame.mixer.Sound("Sound\sound2.ogg").play()

        if 1600 > self.mouse[0] > 400 and 300 > self.mouse[1] > 230:
            if self.click[0] == 1:
                pygame.time.delay(100)
                self.MODE_FADE_OUT = True
                self.cover = pygame.Surface(Setting_Value.Display_Set.display_size)
                self.start_time = time.time()
                self.cover.fill(BLACK)
                pygame.mixer.Sound("Sound\sound2.ogg").play()

        self.margin_background = 0
        #self.cover = pygame.image.load("Resource\_cover.png").convert_alpha()
        for image in self.List_Background:
            self.screen.blit(image, [0, self.pos + self.margin_background])
            self.margin_background  += Setting_Value.Display_Set.bg_margin
        #self.screen.blit(self.cover, [0, 0])

        self.margin_background = 0
        
        # When Scroll Up
        if self.MODE_SCROLL_UP:
            self.pos += self.speed
            self.speed += Setting_Value.Display_Set.scroll_speed
            self.alpha_value -= self.alpha_value_change_speed
            self.alpha_value_change_speed += 9
            if self.alpha_value > 0:
                self.alpha_value -=1
            for image in self.List_Background:
                self.screen.blit(image, [0, self.pos + self.margin_background])
                self.margin_background += Setting_Value.Display_Set.bg_margin
            if self.pos ==  -Setting_Value.Display_Set.bg_margin * (self.list_focus):
                self.MODE_SCROLL_UP = False
                self.speed = 0
                self.alpha_value = 180
                pygame.mixer.music.fadeout(1200)

        # When Scroll down
        if self.MODE_SCROLL_DOWN:
            self.pos -= self.speed
            self.speed += Setting_Value.Display_Set.scroll_speed
            self.alpha_value -= self.alpha_value_change_speed
            self.alpha_value_change_speed += 9
            for image in self.List_Background:
                self.screen.blit(image, [0, self.pos + self.margin_background])
                self.margin_background += Setting_Value.Display_Set.bg_margin
            if self.pos == -Setting_Value.Display_Set.bg_margin * self.list_focus:
                self.MODE_SCROLL_DOWN = False
                self.speed = 0
                self.alpha_value = 180
                pygame.mixer.music.fadeout(1200)

        # BGM
        if not pygame.mixer.music.get_busy() and not self.isGameReadyMode():
            pygame.time.delay(50)
            pygame.mixer.music.load(MapList.MapList[self.get_selected_Song()].file)
            pygame.mixer.music.play(0, MapList.MapList[self.get_selected_Song()].highlight + 0.01)
            pygame.mixer.music.set_volume(0.5)

        i = 0
        for title in self.List:
            self.List_font[i] = (self.font3.render(title, True, NOT_SELECTED))
            i +=1
        # only focused item Set Font with WHITE color
        self.List_font[self.list_focus] = self.font2.render(self.List[self.list_focus], True, WHITE)

        # OUTPUT PART
        for i in self.List_font: # song list
            if(i == self.List_font[self.list_focus]):
                self.screen.blit(i, [Setting_Value.Display_Set.title[0], self.start + self.margin])
                self.margin += 240
                continue
            self.screen.blit(i, [Setting_Value.Display_Set.title[0], self.start + self.margin])
            self.margin += 240

        # COUNT Of Songs
        s = "(%d / %d)" %(self.list_focus+1, self.list_count)
        count = self.font4.render(s, True, WHITE)
        count.set_alpha(50)
        self.screen.blit(count, Setting_Value.Display_Set.SongCount)

        # Information Of Song
        self.List_SongInfo[self.list_focus].update()

        # Back Button
        if 75 > self.mouse[0] > 25 and 25 < self.mouse[1] < 50:
            if self.click[0] == 1:
                self.MODE_FADE_OUT = False

    def isGameReadyMode(self, bool = None):
        global MODE_GAME_READY
        if bool == None:
            return MODE_GAME_READY
        MODE_GAME_READY = bool
        return MODE_GAME_READY

    def get_selected_Song(self):
        return self.list_focus

    def get_selected_SongSpeed(self):
        return self.SongSpeed

class TimeBar(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.length = 0
        self.screen = screen
        self.speed = 0

    def update(self):
        self.indicator = pygame.Surface([self.length, 15])
        self.indicator_th = pygame.Surface([1920, 15]) # threshold
        
        self.indicator.set_alpha(50)
        self.indicator_th.set_alpha(50)
        
        self.indicator.fill(COMBO)
        self.indicator_th.fill(COMBO)

        if self.length > 2000: # end of length
            self.speed = 0
        self.length += self.speed
        
        self.screen.blit(self.indicator, (0, 1065)) # 매 프레임 마다 self.speed 만큼 증가
        self.screen.blit(self.indicator_th, (0, 1065))

    def set_endTime(self, _time):
        self.speed = 2000/(_time * 120)
    
    def initialize(self):
        self.length = 0
        self.speed = 0

class SongInfo(pygame.sprite.Sprite):       
    font1 = pygame.font.Font('Resource\Font\InterparkGothicOTFM.otf', 55)
    font2 = pygame.font.Font('Resource\Font\SansJP.otf', 45)
    font3 = pygame.font.Font('Resource\Font\InterparkGothicOTFM.otf', 30)

    def __init__(self, screen, title, artist, album_art, speed, difficulty ,BPM = None):
        pygame.sprite.Sprite.__init__(self)
        self.album_art = pygame.Surface([200, 200])
        self.album_art.set_alpha(0)
        self.screen = screen
        self.artist = artist
        self.title = title
        if len(title) > 16:
            self.title= title[:15]
            self.title += "..."
        self.speed = speed
        self.difficulty = difficulty
        self.BPM = BPM

    def update(self):
        title_txt = self.font1.render(self.title, True, WHITE)
        difficulty_txt = self.font2.render("「lv. " + str(self.difficulty) + "」", True, COMBO)
        artist_txt = self.font3.render(self.artist, True, WHITE)

        #self.screen.blit(self.album_art, Setting_Value.Display_Set.album_art)
        self.screen.blit(title_txt, Setting_Value.Display_Set.title)
        self.screen.blit(artist_txt, Setting_Value.Display_Set.artist)
        self.screen.blit(difficulty_txt, Setting_Value.Display_Set.difficulty)
        return

class FadeOut(threading.Thread):
    def __init__(self, screen, surface):
        threading.Thread.__init__(self)
        self.screen = screen
        self.surface = surface
        self.start_time = 0

    def set_start_time(self, time):
        self.start_time = time

    def run(self):
        while True:
            end_time = time.time()
            gap = end_time - self.start_time
            if gap < 2:
                self.surface.set_alpha(gap * 55)
                self.screen.blit(self.surface, [0, 0])
            else:
                break