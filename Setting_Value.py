class Display_size:
    def __init__(self, type=1):
        if type == 1:
            # About Main Position
            self.display_size = (1920, 1080)
            self.center = (960, 540)
            self.main_btn_start_x =  184
            self.main_btn_start_y = 590
            self.main_btn_option_x = 184
            self.main_btn_option_y = 690
            self.main_btn_exit_x = 184
            self.main_btn_exit_y = 790

            # About SongList Position
            self.easy_x = 1730
            self.easy_y = 30
            self.hard_x = self.easy_x
            self.hard_y = self.easy_y + 80
            self.bg_margin = 1080
            self.scroll_speed = 1080
            self.SongList  = (150, 130)
            self.SongCount = (1810, 1016)
            self.album_art = (160, 220)
            self.title = (200, 515)
            self.artist = (200, 585)
            self.difficulty = (16, 525)

            # About Game_Ready_State Position
            self.SetTheSpeed = (595, 300)
            self.SongSpeed = (665, 350)
            self.plus_x = 745
            self.plus_y = 350
            self.plus = (self.plus_x, self.plus_y)
            self.minus_x = 600
            self.minus_y = 350
            self.minus = (self.minus_x, self.minus_y)
            self.loading = (911, 405)

            # About Game Position
            self.node1_x = 772
            self.node2_x = 897
            self.node3_x = 1022
            self.node4_x = 1147
            self.node_y = 932
            self.drawer = (600, 513)
            self.combo_txt = (865, 315)
            self.combo_th = (846, 380)
            self.score_txt = (950, 540)
            self.combo = (1020, 380)
            self.score = (950, 580)

            self.note_judge_margin = 832
            self.note_init_pos = 0

            # About Game Result
            self.result = (450, 200)

            # About Setting Bar Position
            self.Setting = (1000, 100)
            self.menuBar = (450,768)
            self.menuBar_pos = 916

Display_Set = Display_size()

