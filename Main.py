import pygame
from Player import Player

#Inicio e Musica
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Sons/music.wav")  
pygame.mixer.music.play(-1)  
som_colisao = pygame.mixer.Sound("Sons/hit.wav")

#Definir o nome do jogo!
pygame.display.set_caption("Armys Crashed")

#Formar a Janela e Marcar o FpS!
screen = pygame.display.set_mode((1280,720))    
Clock = pygame.time.Clock()

# Fontes para o código
fonte_titulo = pygame.font.SysFont(None, 150)
fonte_botao = pygame.font.SysFont(None, 37)
fonte_pontuação = pygame.font.SysFont(None, 50)
fonte_vida = pygame.font.SysFont(None,50)
fonte_game_over = pygame.font.SysFont(None,150)
fonte_aviso_game_over = pygame.font.SysFont(None,100)

# Códigos para o Game Over
fim_de_jogo = False
tela_game_over = pygame.Surface((1280, 720), pygame.SRCALPHA)
tela_game_over.fill((0, 0, 0))  # fundo escuro com transparência
mostrar_game_over = fonte_game_over.render("GAME OVER", True, "Red")
aviso_game_over = fonte_aviso_game_over.render("Pressione R para reiniciar", True, "White")
som_game_over_tocado = False
estado_do_jogo = None

def desenha_game_over(screen):
    screen.blit(tela_game_over, (0, 0))
    screen.blit(mostrar_game_over, (310, 170))
    screen.blit(aviso_game_over, (220, 300))

# Surface (Objetos da tela)
surface = pygame.Surface((200,200))
fundo = pygame.image.load("Imagens/Fundo_8.png").convert_alpha()
# boneco = pygame.image.load("Imagens/Hero.png").convert_alpha()
fundo_menu = pygame.image.load("Imagens/Fundo_blur.png").convert_alpha()
bala_RIGHT = pygame.image.load("Imagens/Assets_Balas/BALA_LEFT.png").convert_alpha()
bala_RIGHT1 = pygame.image.load("Imagens/Assets_Balas/BALA_LEFT1.png").convert_alpha()
bala_LEFT = pygame.image.load("Imagens/Assets_Balas/BALA_RIGHT.png").convert_alpha()
bala_LEFT1 = pygame.image.load("Imagens/Assets_Balas/BALA_RIGHT1.png").convert_alpha()
bala_UPSIDE = pygame.image.load("Imagens/Assets_Balas/BALA_UPSIDE.png").convert_alpha()
bala_UPSIDE1 = pygame.image.load("Imagens/Assets_Balas/BALA_UPSIDE1.png").convert_alpha()
bala_DOWN = pygame.image.load("Imagens/Assets_Balas/BALA_DOWN.png").convert_alpha()
bala_DOWN1 = pygame.image.load("Imagens/Assets_Balas/BALA_DOWN1.png").convert_alpha()

#Pontuação
pontuação = 0
vidas = 3

#Convertendo o tamanho da imagem 
fundo = pygame.transform.scale(fundo,(1280,720))
# boneco = pygame.transform.scale(boneco,(180,180))
fundo_menu = pygame.transform.scale(fundo_menu,(1280,720))
bala_RIGHT = pygame.transform.scale(bala_RIGHT,(90,50))
bala_RIGHT1 = pygame.transform.scale(bala_RIGHT1,(90,50))
bala_LEFT = pygame.transform.scale(bala_LEFT,(90,50))
bala_LEFT1 = pygame.transform.scale(bala_LEFT1,(90,50))
bala_UPSIDE = pygame.transform.scale(bala_UPSIDE,(50,90))
bala_UPSIDE1 = pygame.transform.scale(bala_UPSIDE1,(50,90))
bala_DOWN = pygame.transform.scale(bala_DOWN,(50,90))
bala_DOWN1 = pygame.transform.scale(bala_DOWN1,(50,90))


#Personagem
boneco = Player()
chao_y = 410


#Criando os Retângulos
bala_RIGHT_Rect = bala_RIGHT.get_rect(bottomright = (1000,600))
bala_RIGHT1_Rect = bala_RIGHT1.get_rect(bottomright = (2000,900))
bala_LEFT_Rect = bala_LEFT.get_rect(bottomright = (1300,300))
bala_LEFT1_Rect = bala_LEFT1.get_rect(bottomright = (2000,500))
bala_UPSIDE_Rect = bala_UPSIDE.get_rect(midbottom = (1100,1500))
bala_UPSIDE1_Rect = bala_UPSIDE1.get_rect(midbottom = (1500,2000))
bala_DOWN_Rect = bala_DOWN.get_rect(midtop = (300,-300))
bala_DOWN1_Rect = bala_DOWN1.get_rect(midtop = (750,-600))

#Colisão precisa( Formando mascara, descarta os tranparentes)
# boneco_mask = pygame.mask.from_surface(boneco)
bala_RIGHT_mask = pygame.mask.from_surface(bala_RIGHT)
bala_RIGHT1_mask = pygame.mask.from_surface(bala_RIGHT1)
bala_LEFT_mask = pygame.mask.from_surface(bala_LEFT)
bala_LEFT1_mask = pygame.mask.from_surface(bala_LEFT1)
bala_UPSIDE_mask = pygame.mask.from_surface(bala_UPSIDE)
bala_UPSIDE1_mask = pygame.mask.from_surface(bala_UPSIDE1)
bala_DOWN_mask = pygame.mask.from_surface(bala_DOWN)
bala_DOWN1_mask = pygame.mask.from_surface(bala_DOWN1)
boneco_mask = pygame.mask.from_surface(boneco.current_image)

#Gravidade e estado inicial
gravidadedoboneco = 0
estado_do_jogo = "menu"

while True:

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    
    #Serve para conseguir parar o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:

                    vidas = 3
                    pontuação = 0
                    boneco.rect.x, boneco.rect.y = 601, 498
                    bala_RIGHT_Rect.x = 1300
                    estado_do_jogo = "jogo"
                    pygame.mixer.music.load("Sons/music.wav")
                    pygame.mixer.music.play(-1)
        
        

    #Serve para iniciar o menu
    if estado_do_jogo == "menu":
        screen.blit(fundo_menu, (0, 0))  

    #Escrita na tela /Desenha o texto na tela 
    titulo = fonte_titulo.render("Armys Crashed", True, (255,255,255))
    screen.blit(titulo, (1280//2 - titulo.get_width()//2, 150))

    botao_rect = pygame.Rect(540, 350, 200, 80)
    pygame.draw.rect(screen, (0,128,0), botao_rect)
    texto_botao = fonte_botao.render("JOGAR", True, (255,255,255))
    screen.blit(texto_botao, (botao_rect.x + 60, botao_rect.y + 20))

    if botao_rect.collidepoint(mouse) and click[0]:
        estado_do_jogo = "jogo"

    elif estado_do_jogo == "jogo":

        
        #Adicionar elementos na tela
        #Direita = aumenta o x
        #Baixo = aumenta o y
        screen.blit(surface,(100,100))
        screen.blit(fundo,(0,0))
        boneco.draw(screen)
        screen.blit(bala_LEFT,bala_LEFT_Rect)
        screen.blit(bala_LEFT1,bala_LEFT1_Rect)
        screen.blit(bala_RIGHT,bala_RIGHT_Rect)
        screen.blit(bala_RIGHT1,bala_RIGHT1_Rect)
        screen.blit(bala_UPSIDE,bala_UPSIDE_Rect)
        screen.blit(bala_UPSIDE1,bala_UPSIDE1_Rect)
        screen.blit(bala_DOWN,bala_DOWN_Rect)
        screen.blit(bala_DOWN1,bala_DOWN1_Rect)


        #Movimento bala_LEFT
        bala_LEFT_Rect.x += 5
        if bala_LEFT_Rect.x >= 1920:
            bala_LEFT_Rect.x = -1200
              

        bala_LEFT1_Rect.x += 5
        if bala_LEFT1_Rect.x >= 2300:
            bala_LEFT1_Rect.x = -800
               

        #Movimento bala_DOWN
        bala_DOWN_Rect.y += 5
        if bala_DOWN_Rect.y >= 1900:
            bala_DOWN_Rect.y = -200
            

        bala_DOWN1_Rect.y += 5
        if bala_DOWN1_Rect.y >= 2100:
            bala_DOWN1_Rect.y = -500
             
   
        #Movimento bala_UPSIDE
        bala_UPSIDE_Rect.y -=5
        if bala_UPSIDE_Rect.y <= -1900:
            bala_UPSIDE_Rect.y = 1500
              

        bala_UPSIDE1_Rect.y -=5
        if bala_UPSIDE1_Rect.y <= -2100:
            bala_UPSIDE1_Rect.y = 1700
             
            
        #Movimento bala_RIGHT
        bala_RIGHT_Rect.x -=5
        if bala_RIGHT_Rect.x <= -600:
            bala_RIGHT_Rect.x = 1300
              

        bala_RIGHT1_Rect.x -=5
        if bala_RIGHT1_Rect.x <= -6000:
            bala_RIGHT1_Rect.x = 1700
             



        #Pontuação
        pontuação += 0.1
        textSurface = fonte_pontuação.render(f"PONTUAÇÃO: {int(pontuação)}", False, "White")
        screen.blit(textSurface, (500,50))
        textVidas = fonte_vida.render(f"Vidas {vidas}    |", False, "White")
        screen.blit(textVidas,(300,50))
        
       
        
    
        #Colisão por mascara(mais efetiva)
        offset_UPSIDE = (bala_UPSIDE_Rect.x - boneco.rect.x, bala_UPSIDE_Rect.y - boneco.rect.y)
        if boneco_mask.overlap(bala_UPSIDE_mask,offset_UPSIDE):
            print("Bateu!!!")
            vidas-=1
            bala_UPSIDE_Rect.y = 1500
            som_colisao.play()  

        offset_UPSIDE1 = (bala_UPSIDE1_Rect.x - boneco.rect.x, bala_UPSIDE1_Rect.y - boneco.rect.y)
        if boneco_mask.overlap(bala_UPSIDE1_mask,offset_UPSIDE1):
            print("Bateu!!!")
            vidas-=1
            bala_UPSIDE1_Rect.y = 1700
            som_colisao.play()  

        offset_DOWN =(bala_DOWN_Rect.x - boneco.rect.x, bala_DOWN_Rect.y - boneco.rect.y)
        if boneco_mask.overlap(bala_DOWN_mask,offset_DOWN):
            print("Bateu!!!")
            vidas -=1
            bala_DOWN_Rect.y = -200
            som_colisao.play()  

        offset_DOWN1 =(bala_DOWN1_Rect.x - boneco.rect.x, bala_DOWN1_Rect.y - boneco.rect.y)
        if boneco_mask.overlap(bala_DOWN1_mask,offset_DOWN1):
            print("Bateu!!!")
            vidas -=1
            bala_DOWN1_Rect.y = -500
            som_colisao.play()  

        offset_RIGHT = (bala_RIGHT_Rect.x - boneco.rect.x, bala_RIGHT_Rect.y - boneco.rect.y)
        if boneco_mask.overlap(bala_RIGHT_mask,offset_RIGHT):
            print("Bateu!!!")
            vidas -=1
            bala_RIGHT_Rect.x = 1300
            som_colisao.play()  

        offset_RIGHT1 = (bala_RIGHT1_Rect.x - boneco.rect.x, bala_RIGHT1_Rect.y - boneco.rect.y)
        if boneco_mask.overlap(bala_RIGHT1_mask,offset_RIGHT1):
            print("Bateu!!!")
            vidas -=1
            bala_RIGHT1_Rect.x = 1600
            som_colisao.play()  

        offset_LEFT = (bala_LEFT_Rect.x - boneco.rect.x, bala_LEFT_Rect.y - boneco.rect.y)
        if boneco_mask.overlap(bala_LEFT_mask, offset_LEFT):
            print("Bateu!!!")
            vidas -=1
            bala_LEFT_Rect.x = -300
            som_colisao.play()  

        offset_LEFT1 = (bala_LEFT1_Rect.x - boneco.rect.x, bala_LEFT1_Rect.y - boneco.rect.y)
        if boneco_mask.overlap(bala_LEFT1_mask, offset_LEFT1):
            print("Bateu!!")
            vidas -=1
            bala_LEFT1_Rect.x = -500
            som_colisao.play()  

        if vidas <= 0:
            estado_do_jogo = "game_over"
            pygame.mixer.music.stop()
        
        #Movimento do Jogador e Gravidade
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and boneco.rect.y >= 355:
            gravidadedoboneco = -15
        if key[pygame.K_w] and boneco.rect.y >=355:
            gravidadedoboneco = -15

        gravidadedoboneco += 0.5
        boneco.rect.y += gravidadedoboneco

        if boneco.rect.y > 355:
            boneco.rect.y = 355
            gravidadedoboneco = 0

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            boneco.rect.x += 5
            boneco.RIGHT_KEY = True
            boneco.LEFT_KEY = False
            boneco.FACING_RIGHT = True
            boneco.FACING_LEFT = False

        elif key[pygame.K_LEFT] or key[pygame.K_a]:
            boneco.rect.x -= 5
            boneco.LEFT_KEY = True
            boneco.RIGHT_KEY = False
            boneco.FACING_LEFT = True
            boneco.FACING_RIGHT = False
        else:
            boneco.RIGHT_KEY = False
            boneco.LEFT_KEY = False
    #Estado de jogo game over
    elif estado_do_jogo == "game_over":
        desenha_game_over(screen)

        if not som_game_over_tocado: 
            pygame.mixer.music.load("Sons/game_over.wav")
            pygame.mixer.music.play(1)
            som_game_over_tocado = True

        

        

    #Atualizando a tela a cada mudança e fps=60
    pygame.display.update()
    Clock.tick(60)
    boneco.update()
    boneco.draw(screen)