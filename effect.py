import pyganim

note_anim1 = pyganim.PygAnimation([("Resource\effect\light1.png", 0.01), # node beam
                                   ("Resource\effect\light2.png", 0.02),
                                   ("Resource\effect\light3.png", 0.03),
                                   ("Resource\effect\light4.png", 1),
                                   ("Resource\effect\light3.png", 0.03),
                                   ("Resource\effect\light2.png", 0.02),
                                   ("Resource\effect\light1.png", 0.01)
                                   ], loop=False)
note_anim2 = pyganim.PygAnimation([("Resource\effect\light1.png", 0.01),
                                   ("Resource\effect\light2.png", 0.02),
                                   ("Resource\effect\light3.png", 0.03),
                                   ("Resource\effect\light4.png", 1),
                                   ("Resource\effect\light3.png", 0.03),
                                   ("Resource\effect\light2.png", 0.02),
                                   ("Resource\effect\light1.png", 0.01)
                                   ], loop=False)
note_anim3 = pyganim.PygAnimation([("Resource\effect\light1.png", 0.01),
                                   ("Resource\effect\light2.png", 0.02),
                                   ("Resource\effect\light3.png", 0.03),
                                   ("Resource\effect\light4.png", 1),
                                   ("Resource\effect\light3.png", 0.03),
                                   ("Resource\effect\light2.png", 0.02),
                                   ("Resource\effect\light1.png", 0.01)
                                   ], loop=False)
note_anim4 = pyganim.PygAnimation([("Resource\effect\light1.png", 0.01),
                                   ("Resource\effect\light2.png", 0.02),
                                   ("Resource\effect\light3.png", 0.03),
                                   ("Resource\effect\light4.png", 1),
                                   ("Resource\effect\light3.png", 0.03),
                                   ("Resource\effect\light2.png", 0.02),
                                   ("Resource\effect\light1.png", 0.01)
                                   ], loop=False)

note_anim1.set_colorkey((255,255,255))
note_anim1.set_alpha(50)

note_anim2.set_colorkey((255,255,255))
note_anim2.set_alpha(50)

note_anim3.set_colorkey((255,255,255))
note_anim3.set_alpha(50)

note_anim4.set_colorkey((255,255,255))
note_anim4.set_alpha(50)

bomb_anim1 = pyganim.PygAnimation([(r"Resource\effect\bomb01.png", 0.02), # node bomb
                                   (r"Resource\effect\bomb02.png", 0.02),
                                   (r"Resource\effect\bomb03.png", 0.02),
                                   (r"Resource\effect\bomb04.png", 0.02),
                                   (r"Resource\effect\bomb05.png", 0.02),
                                   (r"Resource\effect\bomb06.png", 0.02),
                                   (r"Resource\effect\bomb07.png", 0.02),
                                   (r"Resource\effect\bomb08.png", 0.02),
                                   (r"Resource\effect\bomb09.png", 0.02),
                                   (r"Resource\effect\bomb10.png", 0.02),
                                   (r"Resource\effect\bomb11.png", 0.02),
                                   (r"Resource\effect\bomb12.png", 0.02),
                                   (r"Resource\effect\bomb13.png", 0.02),
                                   (r"Resource\effect\bomb14.png", 0.02),
                                   (r"Resource\effect\bomb15.png", 0.02),
                                   (r"Resource\effect\bomb16.png", 0.02),
                                   (r"Resource\effect\bomb17.png", 0.02),
                                   (r"Resource\effect\bomb18.png", 0.02),
                                   (r"Resource\effect\bomb19.png", 0.02),
                                   (r"Resource\effect\bomb20.png", 0.02)
                                   ], loop=False)
bomb_anim2 = pyganim.PygAnimation([(r"Resource\effect\bomb01.png", 0.02),
                                   (r"Resource\effect\bomb02.png", 0.02),
                                   (r"Resource\effect\bomb03.png", 0.02),
                                   (r"Resource\effect\bomb04.png", 0.02),
                                   (r"Resource\effect\bomb05.png", 0.02),
                                   (r"Resource\effect\bomb06.png", 0.02),
                                   (r"Resource\effect\bomb07.png", 0.02),
                                   (r"Resource\effect\bomb08.png", 0.02),
                                   (r"Resource\effect\bomb09.png", 0.02),
                                   (r"Resource\effect\bomb10.png", 0.02),
                                   (r"Resource\effect\bomb11.png", 0.02),
                                   (r"Resource\effect\bomb12.png", 0.02),
                                   (r"Resource\effect\bomb13.png", 0.02),
                                   (r"Resource\effect\bomb14.png", 0.02),
                                   (r"Resource\effect\bomb15.png", 0.02),
                                   (r"Resource\effect\bomb16.png", 0.02),
                                   (r"Resource\effect\bomb17.png", 0.02),
                                   (r"Resource\effect\bomb18.png", 0.02),
                                   (r"Resource\effect\bomb19.png", 0.02),
                                   (r"Resource\effect\bomb20.png", 0.02)
                                   ], loop=False)
bomb_anim3 = pyganim.PygAnimation([(r"Resource\effect\bomb01.png", 0.02),
                                   (r"Resource\effect\bomb02.png", 0.02),
                                   (r"Resource\effect\bomb03.png", 0.02),
                                   (r"Resource\effect\bomb04.png", 0.02),
                                   (r"Resource\effect\bomb05.png", 0.02),
                                   (r"Resource\effect\bomb06.png", 0.02),
                                   (r"Resource\effect\bomb07.png", 0.02),
                                   (r"Resource\effect\bomb08.png", 0.02),
                                   (r"Resource\effect\bomb09.png", 0.02),
                                   (r"Resource\effect\bomb10.png", 0.02),
                                   (r"Resource\effect\bomb11.png", 0.02),
                                   (r"Resource\effect\bomb12.png", 0.02),
                                   (r"Resource\effect\bomb13.png", 0.02),
                                   (r"Resource\effect\bomb14.png", 0.02),
                                   (r"Resource\effect\bomb15.png", 0.02),
                                   (r"Resource\effect\bomb16.png", 0.02),
                                   (r"Resource\effect\bomb17.png", 0.02),
                                   (r"Resource\effect\bomb18.png", 0.02),
                                   (r"Resource\effect\bomb19.png", 0.02),
                                   (r"Resource\effect\bomb20.png", 0.02)
                                   ], loop=False)
bomb_anim4 = pyganim.PygAnimation([(r"Resource\effect\bomb01.png", 0.02),
                                   (r"Resource\effect\bomb02.png", 0.02),
                                   (r"Resource\effect\bomb03.png", 0.02),
                                   (r"Resource\effect\bomb04.png", 0.02),
                                   (r"Resource\effect\bomb05.png", 0.02),
                                   (r"Resource\effect\bomb06.png", 0.02),
                                   (r"Resource\effect\bomb07.png", 0.02),
                                   (r"Resource\effect\bomb08.png", 0.02),
                                   (r"Resource\effect\bomb09.png", 0.02),
                                   (r"Resource\effect\bomb10.png", 0.02),
                                   (r"Resource\effect\bomb11.png", 0.02),
                                   (r"Resource\effect\bomb12.png", 0.02),
                                   (r"Resource\effect\bomb13.png", 0.02),
                                   (r"Resource\effect\bomb14.png", 0.02),
                                   (r"Resource\effect\bomb15.png", 0.02),
                                   (r"Resource\effect\bomb16.png", 0.02),
                                   (r"Resource\effect\bomb17.png", 0.02),
                                   (r"Resource\effect\bomb18.png", 0.02),
                                   (r"Resource\effect\bomb19.png", 0.02),
                                   (r"Resource\effect\bomb20.png", 0.02)
                                   ], loop=False)

bomb_anim1.set_colorkey((255,255,255))
bomb_anim1.set_alpha(100)

bomb_anim2.set_colorkey((255,255,255))
bomb_anim2.set_alpha(100)

bomb_anim3.set_colorkey((255,255,255))
bomb_anim3.set_alpha(100)

bomb_anim4.set_colorkey((255,255,255))
bomb_anim4.set_alpha(100)

glow_anim = pyganim.PygAnimation([("Resource\_frame\_frame1.png", 0.01), # frame glow
                                   ("Resource\_frame\_frame2.png", 0.02),
                                   ("Resource\_frame\_frame4.png", 0.06),
                                   ("Resource\_frame\_frame6.png", 0.12)
                                   ], loop=False)

glow_anim.set_colorkey((255,255,255))
glow_anim.set_alpha(128)