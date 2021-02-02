import pygame

pygame.init()

class node(pygame.sprite.Sprite):
    count = 0
    def __init__(self, X, Y, width, height, type, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width,height])
        self.screen = screen
        self.width = width
        self.height = height
        if type == 1:
            self.image = pygame.image.load("Resource\_node\_node1.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(width, height))
        elif type == 2:
            self.image = pygame.image.load("Resource\_node\_node2.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(width, height))
        elif type == 3:
            self.image = pygame.image.load("Resource\_node\_node3.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(width, height))
        elif type == 4:
            self.image = pygame.image.load("Resource\_node\_node4.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(width, height))

        self.rect = self.image.get_rect()
        self.rect.center = (X, Y)

    def update(self, Keypressed, KeyUp, type = 0):
        if type == 1:
            if Keypressed:
                self.image = pygame.image.load("Resource\_node\_node1_hover.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
            elif KeyUp:
                self.image = pygame.image.load("Resource\_node\_node1.png").convert_alpha()
                self.image = pygame.transform.scale(self.image,(self.width, self.height))
        elif type == 2:
            if Keypressed:
                self.image = pygame.image.load("Resource\_node\_node2_hover.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
            elif KeyUp:
                self.image = pygame.image.load("Resource\_node\_node2.png").convert_alpha()
                self.image = pygame.transform.scale(self.image,(self.width, self.height))
        elif type == 3:
            if Keypressed:
                self.image = pygame.image.load("Resource\_node\_node3_hover.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
            elif KeyUp:
                self.image = pygame.image.load("Resource\_node\_node3.png").convert_alpha()
                self.image = pygame.transform.scale(self.image,(self.width, self.height))
        elif type == 4:
            if Keypressed:
                self.image = pygame.image.load("Resource\_node\_node4_hover.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
            elif KeyUp:
                self.image = pygame.image.load("Resource\_node\_node4.png").convert_alpha()
                self.image = pygame.transform.scale(self.image,(self.width, self.height))
