import pygame
import math
import eyed3
import Setting_Value
import time
import effect
import UI

pygame.init()

# Arguments that decide type of notes
Type1 = 1
Type2 = 2
Type3 = 3

temp_score = 0
increase = 0
rest = 0

Killed_Note = 0
Combo = 0
Perfect_count = 0
Great_count = 0
Good_count = 0
Miss_count = 0
Bad_count = 0
isFirstPressed = False
MODE_FADE_OUT = False

flag = 0

class Map(pygame.sprite.Sprite):
    Speed_tuple = (6, 7, 8, 9, 10, 11, 12, 13, 14, 15) # speed value

    def __init__(self, file, title, artist, level, highlight=0, album_art=None, screen=None):
        # Read the Play time of MP3 File
        pygame.sprite.Sprite.__init__(self)
        self.sound = pygame.mixer.Sound(file)
        self.file = file
        self.tag = eyed3.load(file)

        self.song_title = title
        self.artist = artist
        self.playtime = pygame.mixer.Sound.get_length(self.sound) # Second
        self.mode = 1 # Easy 1/ Hard 2
        self.speed = 0

        self.level = level
        # highlight is the time when you want to set
        self.highlight = highlight

        self.note1 = pygame.Surface([15, 65])
        self.note2 = pygame.Surface([15, 65])
        self.note3 = pygame.Surface([15, 65])
        if(album_art != None):
            self.album_art = album_art
        if(screen != None):
            self.screen = screen

        # Easy Mode Map
        self.Group_Note_Map = []
        self.Group_Note_Map_SyncTime = []
        self.Group_LongNote_Map_Length = []
        self.index_map = 0
        self.index_SyncTime = 0
        self.index_LongNote = 0

        # Hard Mode Map, not using
        self.Group_Note_Map_Hard = []
        self.Group_Note_Map_SyncTime_Hard = []
        self.Group_LongNote_Map_Length_Hard = []
        self.index_map_Hard = 0
        self.index_SyncTime_Hard = 0
        self.index_LongNote_Hard = 0

    def add_note(self, type, sync_time, length = None): # add easy mode note
        self.Group_Note_Map.append(type)
        self.Group_Note_Map_SyncTime.append(sync_time)
        if length != None:
            self.Group_LongNote_Map_Length.append(length)
        else:
            self.Group_LongNote_Map_Length.append(0)

    def add_note_hard(self, type, sync_time, length=None): # add hard mode note, not using
        self.Group_Note_Map_Hard.append(type)
        self.Group_Note_Map_SyncTime_Hard.append(sync_time)
        if length != None:
            self.Group_LongNote_Map_Length_Hard.append(length)
        else:
            self.Group_LongNote_Map_Length_Hard.append(0)

    def set_speed(self, i):
        self.speed = self.Speed_tuple[i]

    def set_mode(self, mode):
        self.mode = mode

    def get_title(self):
        return self.song_title

    def get_artist(self):
        return self.artist

    def get_level(self):
        return self.level

    def get_album_artist(self):     
        return self.album_art

    def get_note(self):
        if self.mode == 1:
            return self.Group_Note_Map[self.index_map]
        else:
            return self.Group_Note_Map_Hard[self.index_map_Hard]

    def get_long_note_length(self):
        if self.mode == 1:
            return self.Group_LongNote_Map_Length[self.index_map]
        else:
            return self.Group_LongNote_Map_Length_Hard[self.index_map_Hard]

    def get_sync(self):
        if self.mode == 1:
            return self.Group_Note_Map_SyncTime[self.index_SyncTime]
        else:
            return self.Group_Note_Map_SyncTime_Hard[self.index_SyncTime_Hard]

    def move_sync_index(self):
        if self.mode == 1:
            if self.index_SyncTime < len(self.Group_Note_Map_SyncTime) - 1:
                self.index_SyncTime += 1
                return True
            return False
        else:
            if self.index_SyncTime_Hard < len(self.Group_Note_Map_SyncTime_Hard) - 1:
                self.index_SyncTime_Hard += 1
                return True
            return False

    def move_index(self):
        if self.mode == 1:
            if self.index_map < len(self.Group_Note_Map) - 1:
                self.index_map += 1
        else:
            if self.index_map_Hard < len(self.Group_Note_Map_Hard) - 1:
                self.index_map_Hard += 1

    def get_note_count(self):
        # Last Note is Dummy Note
        if self.mode == 1:
             return self.Group_Note_Map.__len__() - 1
        else:
            return  self.Group_Note_Map_Hard.__len__() - 1

    def init_index(self):
        self.index_SyncTime = 0
        self.index_map = 0
        self.index_LongNote = 0

        self.index_SyncTime_Hard = 0
        self.index_map_Hard = 0
        self.index_LongNote_Hard = 0


class note(pygame.sprite.Sprite):
    Killed_Note = 0
    Combo = 0
    onCount = 0
    MODE_FADE_OUT = None
    is_killed = False

    def __init__(self, screen, width, height, type, speed = 10):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.screen = screen
        self.width = width
        if type == 1:
            self.image = pygame.image.load("Resource\_note\_note.png").convert_alpha()
        elif type == 2:
            self.image = pygame.image.load("Resource\_note\_note.png").convert_alpha()
        elif type == 3:
            self.image = pygame.image.load("Resource\_note\_note.png").convert_alpha()
        else:
            self.image = pygame.image.load("Resource\_note\_note.png").convert_alpha()
            
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.y = Setting_Value.Display_Set.note_init_pos # 0
        self.type = type
        self.LongNote_judge = 3

        # note position
        if type == 1:
            self.rect.x = Setting_Value.Display_Set.node1_x - 50
        elif type == 2:
            self.rect.x = Setting_Value.Display_Set.node2_x - 50
        elif type == 3:
            self.rect.x = Setting_Value.Display_Set.node3_x - 50
        elif type == 4:
            self.rect.x = Setting_Value.Display_Set.node4_x - 50
        
    def update(self, type = 0, KeyPressed = False, KeyUp = False):
        self.rect.y += self.speed

        if self.note_fade_out():
            if self.onCount == 0:
                # When This Loop Was First Called, init the start_time
                self.start_time = time.time()
            end_time = time.time() - self.start_time
            #self.image.set_alpha(255 - (end_time * 555))
            self.onCount += 1
            if end_time > 0:
                self.kill()
                killed_note(1)
                self.onCount = 0
                self.note_fade_out(False)
            return
        if self.rect.y > Setting_Value.Display_Set.note_judge_margin:
            #print('fade')
            self.note_fade()
        
        if Setting_Value.Display_Set.note_judge_margin - 50 > self.rect.y > Setting_Value.Display_Set.note_judge_margin - 52 and KeyPressed and self.type == type and not self.is_killed:
            #print('miss')
            UI.ALPHA = 0
            UI.BLPHA = 900
            combo(0, True)
            self.note_fade_out(True)
            #self.glow_frame()
            score(3)
            self.judge = "BAD"
            bad(1)
        elif Setting_Value.Display_Set.note_judge_margin - 30 >= self.rect.y > Setting_Value.Display_Set.note_judge_margin - 50 and KeyPressed and self.type == type and not self.is_killed:
            #print('great')
            self.note_bomb()
            UI.ALPHA = 0
            UI.BLPHA = 900
            combo(1)
            self.note_fade_out(True)
            #self.glow_frame()
            score(2)
            self.judge = "GREAT"
            great(1)
        elif Setting_Value.Display_Set.note_judge_margin + 60 >= self.rect.y > Setting_Value.Display_Set.note_judge_margin - 30 and KeyPressed and self.type == type and not self.is_killed:
            #print('perfect')
            self.note_bomb()
            UI.ALPHA = 0
            UI.BLPHA = 900
            combo(1)
            self.note_fade_out(True)
            #self.glow_frame()
            score(1)
            self.judge = "PERFECT"
            perfect(1)
        elif Setting_Value.Display_Set.note_judge_margin + 120 >= self.rect.y > Setting_Value.Display_Set.note_judge_margin + 60 and KeyPressed and self.type == type and not self.is_killed:
            #print('good')
            self.note_bomb()
            UI.ALPHA = 0
            UI.BLPHA = 900
            combo(1)
            self.note_fade_out(True)
            #self.glow_frame()
            score(2)
            self.judge = "GOOD"
            good(1)
        elif self.rect.y > Setting_Value.Display_Set.note_judge_margin + 120 and not self.is_killed:
            #print('miss3')
            UI.ALPHA = 0
            UI.BLPHA = 900
            combo(0,True)
            self.note_fade_out(True)
            #self.glow_frame()
            score(3)
            self.judge = "MISS"
            miss(1)

    def re_init(self):
        self.alive()
        self.rect.y = Setting_Value.Display_Set.note_init_pos

    def note_fade(self): # only alpha
        self.image.set_alpha(25)
        
    def note_fade_out(self, bool = None): # note kill
        if bool == None:
            return self.MODE_FADE_OUT
        self.MODE_FADE_OUT = bool
        self.is_killed = True
        return self.MODE_FADE_OUT
    
    def note_bomb(self):
        if self.type == 1:
            effect.bomb_anim1.play()
        elif self.type == 2:
            effect.bomb_anim2.play()
        elif self.type == 3:
            effect.bomb_anim3.play()
        elif self.type == 4:
            effect.bomb_anim4.play()
    
    '''
    def glow_frame(self):
        effect.glow_anim.play()
    '''

def combo(increase, init = False): # calc combo count
    global Combo
    if init:
        Combo = 0
    Combo += increase
    return Combo

def killed_note(increase, init = False): # calc killed note count
    global Killed_Note
    if init:
        Killed_Note = 0
    Killed_Note += increase
    return Killed_Note

def judge(): # 판정
    global flag
    if flag == 0:
        return "MISS", (128, 128, 192), (885, 560)
    elif flag == 1:
        return "GREAT", (128, 255, 255), (865, 560)
    elif flag == 2:
        return "PERFECT", (255, 255, 128), (827, 560)
    elif flag == 3:
        return "GOOD", (255, 128, 255), (885, 560)
    elif flag == 4:
        return "BAD", (128, 128, 128), (905, 560)

def perfect(increase, init = False): # calc perfect count
    global Perfect_count
    global flag
    if init:
        Perfect_count = 0
    Perfect_count += 1
    flag = 2
    return Perfect_count

def good(increase, init = False): # calc good count
    global Good_count
    global flag
    if init:
        Good_count = 0
    Good_count += 1
    flag = 3
    return Good_count

def great(increase, init = False): # calc great count
    global Great_count
    global flag
    if init:
        Great_count = 0
    Great_count += 1
    flag = 1
    return Great_count

def bad(increase, init = False): # calc bad count
    global Bad_count
    global flag
    if init:
        Bad_count = 0
    Bad_count += 1
    flag = 4
    return Bad_count

def miss(increase, init = False): # calc miss count
    global Miss_count
    global flag
    if init:
        Miss_count = 0
    Miss_count += 1
    flag = 0
    return Miss_count


def is_first_pressed(bool): # 
    global isFirstPressed
    isFirstPressed = bool
    return isFirstPressed


def score(__type, selected_map=None): # calc score
    global temp_score
    global rest
    global increase
    if __type == -1:
        # INIT
        temp_score = 0
        rest = 0
        increase = 0

    if not selected_map == None:
        rest = math.fmod(100000, selected_map.get_note_count())
        increase = (100000 - rest) / selected_map.get_note_count() # calc score of one note

    if __type == 1: # PERFECT
        temp_score += increase
    elif __type == 2: # GREAT
        temp_score += (increase / 10) * 8
    elif __type == 3: # MISS, BAD
        temp_score += 0

    return int(temp_score)

def result():
    global temp_score
    global Perfect_count
    global Great_count
    global Good_count
    global Bad_count
    global Miss_count
    
    score = int(temp_score)
    count = (Perfect_count, Great_count, Good_count, Bad_count, Miss_count)
    
    if score == 100000:
        return score, "S", (255, 255, 64), count
    elif score > 80000:
        return score, "A", (64, 255, 255), count
    elif score > 60000:
        return score, "B", (255, 255, 64), count
    elif score > 40000:
        return score, "C", (128, 128, 192), count
    else:
        return score, "D", (128, 128, 128), count

def initialize():
    global temp_score
    global Perfect_count
    global Great_count
    global Good_count
    global Bad_count
    global Miss_count
    
    # initialize
    temp_score = 0
    Perfect_count = 0
    Great_count = 0
    Good_count = 0
    Bad_count = 0
    Miss_count = 0