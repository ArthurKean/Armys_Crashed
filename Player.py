import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT, self.FACING_RIGHT = False, False, False, False
        self.load_frames()
        self.rect = self.idle_frames_left[0].get_rect()
        self.rect.midbottom = (600,300)
        self.current_frame = 0
        self.last_update = 0
        self.velocity = 0
        self.state = "idle"
        self.current_image = self.idle_frames_left[0]
        
  

    def update(self):
        self.velocity = 0
        if self.LEFT_KEY:
            self.velocity = -2
        elif self.RIGHT_KEY:
            self.velocity = 2 
        self.rect.x += self.velocity
        self.set_state()
        self.animate()

    def draw(self,screen):
         screen.blit(self.current_image, self.rect)

    def animate(self):
        now = pygame.time.get_ticks()
        if self.state == "idle":
            if now - self.last_update > 120:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames_right)
                if self.FACING_LEFT:
                    self.current_image = self.idle_frames_left[self.current_frame]
                elif  self.FACING_RIGHT:
                    self.current_image = self.idle_frames_right[self.current_frame]
        else:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames_right)
                if self.state == "moving right":
                    self.current_image = self.walking_frames_right[self.current_frame]
                elif self.state == "moving left":
                    self.current_image = self.walking_frames_left[self.current_frame]

    def set_state(self):
        self.state = "idle"
        if self.velocity > 0:
            self.state = "moving right"
        elif self.velocity < 0:
            self.state = "moving left"

    def load_frames(self):
        
        self.idle_frames_right = [pygame.image.load("Imagens/Boneco_Assets/_0009_Idle-hero01_001.png.png").convert_alpha(),
                                 pygame.image.load("Imagens/Boneco_Assets/_0010_Idle-hero01_002.png.png").convert_alpha(),
                                 pygame.image.load("Imagens/Boneco_Assets/_0011_Idle-hero01_003.png.png").convert_alpha(),
                                 pygame.image.load("Imagens/Boneco_Assets/_0012_Idle-hero01_004.png.png").convert_alpha(),
                                 pygame.image.load("Imagens/Boneco_Assets/_0013_Idle-hero01_005.png.png").convert_alpha(),
                                 pygame.image.load("Imagens/Boneco_Assets/_0014_Idle-hero01_006.png.png").convert_alpha(),
                                 pygame.image.load("Imagens/Boneco_Assets/_0015_Idle-hero01_007.png.png").convert_alpha(),
                                 pygame.image.load("Imagens/Boneco_Assets/_0016_Idle-hero01_008.png.png").convert_alpha(),
                                 pygame.image.load("Imagens/Boneco_Assets/_0017_Idle-hero01_009.png.png").convert_alpha()
                                 ]
        
        self.walking_frames_right = [pygame.image.load("Imagens/Boneco_Assets/Run-hero01_001.png").convert_alpha(),
                                    pygame.image.load("Imagens/Boneco_Assets/Run-hero01_002.png").convert_alpha(),
                                    pygame.image.load("Imagens/Boneco_Assets/Run-hero01_003.png").convert_alpha(),
                                    pygame.image.load("Imagens/Boneco_Assets/Run-hero01_004.png").convert_alpha(),
                                    pygame.image.load("Imagens/Boneco_Assets/Run-hero01_005.png").convert_alpha(),
                                    pygame.image.load("Imagens/Boneco_Assets/Run-hero01_006.png").convert_alpha(),
                                    pygame.image.load("Imagens/Boneco_Assets/Run-hero01_007.png").convert_alpha()
                                    ]
        
        self.idle_frames_left = []
        for frame in self.idle_frames_right:
            self.idle_frames_left.append(pygame.transform.flip(frame,True,False))
        
        self.walking_frames_left = []
        for frame in self.walking_frames_right:
            self.walking_frames_left.append(pygame.transform.flip(frame,True,False))