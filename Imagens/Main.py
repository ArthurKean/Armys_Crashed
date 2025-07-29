import pygame
from Player import Player

pygame.init()
pygame.display.set_caption("Armys Crashed")

#Formar a Janela e Marcar o FpS
screen = pygame.display.set_mode((1280,720))    
Clock = pygame.time.Clock()

# Fontes para menu
fonte_titulo = pygame.font.SysFont(None, 150)
fonte_botao = pygame.font.SysFont(None, 37)
fonte_pontuação = pygame.font.SysFont(None, 50)
fonte_vida = pygame.font.SysFont(None,50)
fonte_game_over = pygame.font.SysFont(None,150)
fonte_aviso_game_over = pygame.font.SysFont(None,100)

#Fim de Jogo

fim_de_jogo = False
tela_game_over = pygame.Surface((1280, 720), pygame.SRCALPHA)
tela_game_over.fill((0, 0, 0))  # fundo escuro com transparência
mostrar_game_over = fonte_game_over.render("GAME OVER", True, "Red")
aviso_game_over = fonte_aviso_game_over.render("Pressione R para reiniciar", True, "White")

def desenha_game_over(screen):
    screen.blit(tela_game_over, (0, 0))
    screen.blit(mostrar_game_over, (310, 170))
    screen.blit(aviso_game_over, (220, 300))

# Surface (Objetos da tela)
surface = pygame.Surface((200,200))
fundo = pygame.image.load("Imagens/Fundo_8.png").convert_alpha()
boneco = pygame.image.load("Imagens/Hero.png").convert_alpha()
fundo_menu = pygame.image.load("Imagens/Fundo_blur.png").convert_alpha()
bala_RIGHT = pygame.image.load("Imagens/Assets_Balas/BALA_RIGHT.png").convert_alpha()
bala_LEFT = pygame.image.load("Imagens/Assets_Balas/BALA_LEFT.png").convert_alpha()
bala_UPSIDE = pygame.image.load("Imagens/Assets_Balas/BALA_UPSIDE.png").convert_alpha()
bala_DOWN = pygame.image.load("Imagens/Assets_Balas/BALA_DOWN.png").convert_alpha()

#Pontuação
pontuação = 0
vidas = 3

#Convertendo o tamanho da imagem 
fundo = pygame.transform.scale(fundo,(1280,720))
boneco = pygame.transform.scale(boneco,(180,180))
fundo_menu = pygame.transform.scale(fundo_menu,(1280,720))


#Personagem
boneco = Player()
chao_y = 410


#Criando os Retângulos
bala_RIGHT_Rect = bala_RIGHT.get_rect(bottomright = (1300,300))
bala_LEFT_Rect = bala_LEFT.get_rect(bottomright = (1300,300))
bala_UPSIDE_Rect = bala_UPSIDE.get_rect(bottomright = (1300,300))
bala_DOWN_Rect = bala_DOWN.get_rect(bottomright = (1300,300))

#Colisão precisa( Formando mascara, descarta os tranparentes)
# boneco_mask = pygame.mask.from_surface(boneco)
bala_RIGHT_mask = pygame.mask.from_surface(bala_RIGHT)
bala_LEFT_mask = pygame.mask.from_surface(bala_LEFT)
bala_UPSIDE_mask = pygame.mask.from_surface(bala_UPSIDE)
bala_DOWN_mask = pygame.mask.from_surface(bala_DOWN)
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

    #Serve para iniciar o menu
    if estado_do_jogo == "menu":
        screen.blit(fundo_menu, (0, 0))  

    #Escrita na tela /Desenha o texto na tela para que fique centralizado na largura, e 150 pixels de distância do topo
    titulo = fonte_titulo.render("Armys Crashed", True, (255,255,255))
    screen.blit(titulo, (1280//2 - titulo.get_width()//2, 150))

    botao_rect = pygame.Rect(540, 350, 200, 80)
    pygame.draw.rect(screen, (0,128,0), botao_rect)
    texto_botao = fonte_botao.render("JOGAR", True, (255,255,255))
    screen.blit(texto_botao, (botao_rect.x + 60, botao_rect.y + 20))

    if botao_rect.collidepoint(mouse) and click[0]:
        estado_do_jogo = "jogo"

    elif estado_do_jogo == "jogo":

        #JOGO
        #Adicionar elementos na tela
        #Direita = aumenta o x
        #Baixo = aumenta o y
        screen.blit(surface,(100,100))
        screen.blit(fundo,(0,0))
        boneco.draw(screen)
        screen.blit(bala_LEFT,bala_LEFT_Rect)
        screen.blit(bala_RIGHT,bala_RIGHT_Rect)
        screen.blit(bala_UPSIDE,bala_UPSIDE_Rect)
        screen.blit(bala_DOWN,bala_DOWN_Rect)


        #Movimento BALA_LEFT
        bala_LEFT_Rect.x += 5
        if bala_LEFT_Rect.x >= 1500:
            bala_LEFT_Rect.x = -300

        #Movimento Bala
        bala_RIGHT_Rect.x -=5
        if bala_RIGHT_Rect.x <= -600:
            bala_RIGHT_Rect.x = 1300



        #Pontuação
        pontuação += 0.1
        textSurface = fonte_pontuação.render("PONTUAÇÃO: %d" % pontuação, False, "White")
        screen.blit(textSurface, (500,50))
        textVidas = fonte_vida.render("Vidas %d" % vidas, False, "White")
        screen.blit(textVidas,(500,150))
        
        
    
        #Posição relativa
        # offset2 = (balaRect.x - bonecoRect.x, balaRect.y - bonecoRect.y)
        offset2 = (bala_RIGHT_Rect.x - boneco.rect.x, bala_RIGHT_Rect.y - boneco.rect.y)

        if boneco_mask.overlap(bala_RIGHT_mask,offset2):
            print("COLIDIU!!!")
            vidas -=1
            bala_RIGHT_Rect.x = 1300

        offset = (bala_LEFT_Rect.x - boneco.rect.x, bala_LEFT_Rect.y - boneco.rect.y)


        if boneco_mask.overlap(bala_LEFT_mask, offset):
            print("ColidiUUUU")
            vidas -=1
            bala_LEFT_Rect.x = -300

        if vidas <= 0:
            estado_do_jogo = "game_over"
        

        #Serve para eu visulizar os "Retângulos"
        # pygame.draw.rect(screen, (255,0,0), bonecoRect, 2)
        # pygame.draw.rect(screen, (0,255,0), flechaRect, 2)
        # pygame.draw.rect(screen, (255,0,0), balaRect, 2)
        
        #Movimento do Jogador
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and boneco.rect.y >= 355:
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

    elif estado_do_jogo == "game_over":
        desenha_game_over(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Reiniciar o jogo
                    vidas = 3
                    pontuação = 0
                    boneco.rect.x, boneco.rect.y = 601, 498
                    balaRect.x = 1300
                    estado_do_jogo = "jogo"

    #Atualizando a tela a cada mudança e fps=60
    pygame.display.update()
    Clock.tick(60)
    boneco.update()
    boneco.draw(screen)
