import pygame

#Define a classe do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #controle de movimento e direção
        self.LEFT_KEY, self.RIGHT_KEY = False, False
        self.FACING_LEFT, self.FACING_RIGHT = False, False

        #Carrega os sprites/frames de animação
        self.load_frames()

        #Define a área de colisão 
        self.rect = self.idle_frames_left[0].get_rect()
        self.rect.midbottom = (600, 300)  # Posição inicial do boneco

        #Variáveis de controle da animação
        self.current_frame = 0
        self.last_update = 0
        self.velocity = 0
        self.state = "idle"  #Estado inicial
        self.current_image = self.idle_frames_left[0]  # Frame inicial a ser exibido

    def update(self):
        #Atualiza a velocidade horizontal com base nas teclas pressionadas
        self.velocity = 0
        if self.LEFT_KEY:
            self.velocity = -2  # Move para a esquerda
        elif self.RIGHT_KEY:
            self.velocity = 2   # Move para a direita

        #Aplica o movimento horizontal
        self.rect.x += self.velocity

        #Define o estado atual (idle ou andando)
        self.set_state()

        #Atualiza o frame da animação com base no estado
        self.animate()

    #Desenha o personagem na tela
    def draw(self, screen):
        screen.blit(self.current_image, self.rect)

    #Controle de animação
    def animate(self):
        now = pygame.time.get_ticks()  # Tempo atual em milissegundos

        #Animação parado (idle)
        if self.state == "idle":
            if now - self.last_update > 120:  #Atualiza a cada 120ms
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames_right)

                #Define o frame atual com base na direção que está olhando
                if self.FACING_LEFT:
                    self.current_image = self.idle_frames_left[self.current_frame]
                elif self.FACING_RIGHT:
                    self.current_image = self.idle_frames_right[self.current_frame]

        #Animação andando
        else:
            if now - self.last_update > 100:  #Atualiza a cada 100ms
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames_right)

                #Define o frame atual com base no estado
                if self.state == "moving right":
                    self.current_image = self.walking_frames_right[self.current_frame]
                elif self.state == "moving left":
                    self.current_image = self.walking_frames_left[self.current_frame]

    #Define o estado do personagem com base na velocidade atual
    def set_state(self):
        self.state = "idle"
        if self.velocity > 0:
            self.state = "moving right"
        elif self.velocity < 0:
            self.state = "moving left"

    #Carrega os frames de animação (idle e andando)
    def load_frames(self):
        #Carrega os frames da animação parado virado para a direita
        self.idle_frames_right = [
            pygame.image.load("Imagens/Boneco_Assets/_0009_Idle-hero01_001.png.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/_0010_Idle-hero01_002.png.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/_0011_Idle-hero01_003.png.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/_0012_Idle-hero01_004.png.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/_0013_Idle-hero01_005.png.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/_0014_Idle-hero01_006.png.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/_0015_Idle-hero01_007.png.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/_0016_Idle-hero01_008.png.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/_0017_Idle-hero01_009.png.png").convert_alpha()
        ]

        #Carrega os frames da animação andando para a direita
        self.walking_frames_right = [
            pygame.image.load("Imagens/Boneco_Assets/Run-hero01_001.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/Run-hero01_002.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/Run-hero01_003.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/Run-hero01_004.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/Run-hero01_005.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/Run-hero01_006.png").convert_alpha(),
            pygame.image.load("Imagens/Boneco_Assets/Run-hero01_007.png").convert_alpha()
        ]

        #Gera os frames virados para a esquerda
        self.idle_frames_left = [pygame.transform.flip(frame, True, False) for frame in self.idle_frames_right]
        self.walking_frames_left = [pygame.transform.flip(frame, True, False) for frame in self.walking_frames_right]